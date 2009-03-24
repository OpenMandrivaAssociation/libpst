#
#
# Warning !
# The version newer than 0.6.27 have a different ABI than the one used by evolution 2.26 plugin
# Please ensure it's compatible before upgrading
#
#
#

%define	major 1
%define libname	%mklibname pst %{major}
%define develname %mklibname -d pst

Summary:            Utilities to convert Outlook .pst files to other formats
Name:               libpst
Version:            0.6.27
Release:            %mkrel 2
License:            GPLv2+
Group:              Networking/Mail
Source:             http://www.five-ten-sg.com/%{name}/packages/%{name}-%{version}.tar.gz
BuildRoot:          %{_tmppath}/%{name}-%{version}-%{release}
URL:                http://www.five-ten-sg.com/%{name}/
Requires:           ImageMagick
BuildRequires:      ImageMagick
BuildRequires:      freetype-devel
BuildRequires:      gd-devel
BuildRequires:      jpeg-devel
BuildRequires:      zlib-devel
BuildRequires:      gettext-devel
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

%prep
%setup -q

%build
#TODO fix format not a string literal
%define Werror_cflags %nil

%configure2_5x --enable-libpst-shared
%make


%install
rm -rf %{buildroot}
%makeinstall

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
%{_includedir}/libpst/*.h
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/pkgconfig/%{name}.pc


