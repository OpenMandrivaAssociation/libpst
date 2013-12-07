%define	major	4
%define libname	%mklibname pst %{major}
%define devname %mklibname -d pst

Summary:	Utilities to convert Outlook .pst files to other formats
Name:		libpst
Epoch:		1
Version:	0.6.61
Release:	5
License:	GPLv2+
Group:		Networking/Mail
Url:		http://www.five-ten-sg.com/%{name}/
Source0:	http://www.five-ten-sg.com/%{name}/packages/%{name}-%{version}.tar.gz
Patch0:		libpst-0.6.45-linkage.patch

BuildRequires:	imagemagick
BuildRequires:	boost-devel
BuildRequires:	gd-devel
BuildRequires:	gettext-devel
BuildRequires:	jpeg-devel
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(libgsf-1)
BuildRequires:	pkgconfig(python)
BuildRequires:	pkgconfig(zlib)
Requires:	imagemagick
Provides:	pst-utils

%description
The Libpst utilities include readpst which can convert email messages
to both mbox and MH mailbox formats, pst2ldif which can convert the
contacts to .ldif format for import into ldap databases, and pst2dii
which can convert email messages to the DII load file format used by
Summation.

%package -n	%{libname}
Summary:	A shared library for .pst files support
Group:		System/Libraries

%description -n	%{libname}
Library needed for running libpst tools.

%package -n	%{devname}
Summary:	Library and header files for the libpst library
Group:		Development/C
Provides:	%{name}-devel = %{EVRD}
Requires:	%{libname} = %{EVRD}

%description -n	%{devname}
Library and header files for the libpst library.

%package -n	python-%{name}
Summary:	Python binding for the libpst library
Group:		Development/Python
Requires:	%{libname} = %{EVRD}

%description -n	python-%{name}
Python module for using pst files.

%prep
%setup -q
%patch0 -p0

%build
%configure2_5x \
	--disable-static \
	--enable-libpst-shared \
	--enable-shared 

%make LIBS='-lpython2.7'

%install
%makeinstall_std

%files
%{_bindir}/*
%{_mandir}/man1/*
%{_mandir}/man5/*
%docdir %{_datadir}/doc/%{name}-%{version}
%{_datadir}/doc/%{name}-%{version}

%files -n %{libname}
%{_libdir}/libpst.so.%{major}*

%files -n %{devname}
%{_includedir}/libpst-4/
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc

%files -n python-%{name}
%{py_platsitedir}/_libpst.so

