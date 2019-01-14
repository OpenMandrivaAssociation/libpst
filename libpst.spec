%define _disable_lto 1
%define _disable_rebuild_configure 1

%define major 4
%define libname %mklibname pst %{major}
%define devname %mklibname pst -d

Summary:	Utilities to convert Outlook .pst files to other formats
Name:		libpst
Epoch:		1
Version:	0.6.72
Release:	1
License:	GPLv2+
Group:		Networking/Mail
Url:		http://www.five-ten-sg.com/%{name}/
Source0:	http://www.five-ten-sg.com/%{name}/packages/%{name}-%{version}.tar.gz
Patch0:		libpst-0.6.72-linkage.patch
BuildRequires:	imagemagick
BuildRequires:	boost-devel
BuildRequires:	boost-python-devel
BuildRequires:	gd-devel
BuildRequires:	gettext-devel
BuildRequires:	jpeg-devel
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(libgsf-1)
BuildRequires:	pkgconfig(python)
BuildRequires:	pkgconfig(zlib)
Requires:	imagemagick
Provides:	pst-utils = %{EVRD}

%description
The Libpst utilities include readpst which can convert email messages
to both mbox and MH mailbox formats, pst2ldif which can convert the
contacts to .ldif format for import into ldap databases, and pst2dii
which can convert email messages to the DII load file format used by
Summation.

%files
%{_bindir}/*
%{_mandir}/man1/*
%{_mandir}/man5/*
%docdir %{_datadir}/doc/%{name}-%{version}
%{_datadir}/doc/%{name}-%{version}

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	A shared library for .pst files support
Group:		System/Libraries

%description -n %{libname}
Library needed for running libpst tools.

%files -n %{libname}
%{_libdir}/libpst.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Library and header files for the libpst library
Group:		Development/C
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}

%description -n %{devname}
Library and header files for the libpst library.

%files -n %{devname}
%{_includedir}/libpst-4/
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc

#----------------------------------------------------------------------------

%package -n python-%{name}
Summary:	Python binding for the libpst library
Group:		Development/Python
Requires:	%{libname} = %{EVRD}

%description -n python-%{name}
Python module for using pst files.

%files -n python-%{name}
%{py_platsitedir}/_libpst.so

#----------------------------------------------------------------------------

%prep
%setup -q
%autopatch -p1

%build
export CC=gcc
export CXX=g++

#export PYTHON=%{__python2}
%configure \
	--disable-static \
	--enable-libpst-shared \
	--enable-shared

%make_build

%install
%make_install
