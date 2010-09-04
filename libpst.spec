%define	major 4
%define libname	%mklibname pst %{major}
%define develname %mklibname -d pst

Summary:            Utilities to convert Outlook .pst files to other formats
Name:               libpst
Version:            0.6.48
Release:            %mkrel 1
License:            GPLv2+
Group:              Networking/Mail
Source:             http://www.five-ten-sg.com/%{name}/packages/%{name}-%{version}.tar.gz
Patch0:	            libpst-0.6.45-linkage.patch
BuildRoot:          %{_tmppath}/%{name}-%{version}-%{release}
URL:                http://www.five-ten-sg.com/%{name}/
Requires:           ImageMagick
Requires:	    %{libname} = %{epoch}:%{version}
BuildRequires:      ImageMagick
BuildRequires:      freetype-devel
BuildRequires:      gd-devel
BuildRequires:      jpeg-devel
BuildRequires:      zlib-devel
BuildRequires:      gettext-devel
BuildRequires:      python-devel
BuildRequires:      libboost-devel
Obsoletes:	    pst-utils
Provides:	    pst-utils
Epoch:	1

%description
The Libpst utilities include readpst which can convert email messages
to both mbox and MH mailbox formats, pst2ldif which can convert the
contacts to .ldif format for import into ldap databases, and pst2dii
which can convert email messages to the DII load file format used by
Summation.

%package -n	%{libname}
Summary:	A shared library for .pst files support
Group:          System/Libraries

%description -n	%{libname}
Library needed for running libpst tools.

%package -n	%{develname}
Summary:	Library and header files for the libpst library
Group:		Development/C
Provides:	%{name}-devel = %{epoch}:%{version}
Requires:	%{libname} = %{epoch}:%{version}

%description -n	%{develname}
Library and header files for the libpst library.

%package -n python-%name
Summary:	Python binding for the libpst library
Group:		Development/Python
Requires:	%libname = %epoch:%version-%release

%description -n	python-%name
Python module for using pst files.

%prep
%setup -q
%patch0 -p0

%build
%configure2_5x --enable-libpst-shared --enable-shared
%make

%install
rm -rf %{buildroot}
%makeinstall_std
rm -f %buildroot%py_platsitedir/_libpst.a

%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%{_bindir}/*
%{_mandir}/man1/*
%{_mandir}/man5/*
%docdir %{_datadir}/doc/%{name}-%{version}
%{_datadir}/doc/%{name}-%{version}

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%{_includedir}/libpst-4/
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/pkgconfig/%{name}.pc

%files -n python-%name
%defattr(-,root,root)
%py_platsitedir/_libpst.so
%py_platsitedir/_libpst.la
