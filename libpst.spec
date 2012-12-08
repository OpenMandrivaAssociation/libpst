%define	major 4
%define libname	%mklibname pst %{major}
%define develname %mklibname -d pst

Summary:	Utilities to convert Outlook .pst files to other formats
Name:		libpst
Version:	0.6.54
Release:	3
Epoch:		1
License:	GPLv2+
Group:		Networking/Mail
Source:		http://www.five-ten-sg.com/%{name}/packages/%{name}-%{version}.tar.gz
Patch0:		libpst-0.6.45-linkage.patch
URL:		http://www.five-ten-sg.com/%{name}/
Requires:	imagemagick
BuildRequires:	imagemagick
BuildRequires:	freetype-devel
BuildRequires:	gd-devel
BuildRequires:	jpeg-devel
BuildRequires:	zlib-devel
BuildRequires:	gettext-devel
BuildRequires:	python-devel
BuildRequires:	boost-devel
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

%package -n	%{develname}
Summary:	Library and header files for the libpst library
Group:		Development/C
Provides:	%{name}-devel = %{EVRD}
Requires:	%{libname} = %{EVRD}

%description -n	%{develname}
Library and header files for the libpst library.

%package -n python-%{name}
Summary:	Python binding for the libpst library
Group:		Development/Python
Requires:	%{libname} = %{EVRD}

%description -n	python-%{name}
Python module for using pst files.

%prep
%setup -q
%patch0 -p0

%build
%configure2_5x --enable-libpst-shared --enable-shared --disable-static
%make

%install
%makeinstall_std
rm -f %{buildroot}%{py_platsitedir}/_libpst.a

%files
%{_bindir}/*
%{_mandir}/man1/*
%{_mandir}/man5/*
%docdir %{_datadir}/doc/%{name}-%{version}
%{_datadir}/doc/%{name}-%{version}

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%{_includedir}/libpst-4/
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc

%files -n python-%{name}
%{py_platsitedir}/_libpst.so


%changelog
* Sun May 29 2011 Götz Waschk <waschk@mandriva.org> 1:0.6.52-1mdv2011.0
+ Revision: 681739
- update to new version 0.6.52

* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 1:0.6.49-4
+ Revision: 662410
- mass rebuild

* Thu Mar 17 2011 Funda Wang <fwang@mandriva.org> 1:0.6.49-3
+ Revision: 645715
- rebuild for new boost

  + Matthew Dawkins <mattydaw@mandriva.org>
    - disabled static build

* Thu Nov 04 2010 Götz Waschk <waschk@mandriva.org> 1:0.6.49-2mdv2011.0
+ Revision: 593342
- rebuild for new python 2.7

* Wed Sep 29 2010 Götz Waschk <waschk@mandriva.org> 1:0.6.49-1mdv2011.0
+ Revision: 582006
- update to new version 0.6.49

* Sat Sep 04 2010 Götz Waschk <waschk@mandriva.org> 1:0.6.48-1mdv2011.0
+ Revision: 575877
- update to new version 0.6.48

* Mon Aug 23 2010 Funda Wang <fwang@mandriva.org> 1:0.6.47-2mdv2011.0
+ Revision: 572245
- rebuild for new boost

* Sat Aug 07 2010 Götz Waschk <waschk@mandriva.org> 1:0.6.47-1mdv2011.0
+ Revision: 567293
- update to new version 0.6.47

* Thu Aug 05 2010 Funda Wang <fwang@mandriva.org> 1:0.6.46-2mdv2011.0
+ Revision: 566293
- rebuild for new boost

* Tue Feb 16 2010 Götz Waschk <waschk@mandriva.org> 1:0.6.46-1mdv2010.1
+ Revision: 506451
- new version

* Mon Feb 08 2010 Anssi Hannula <anssi@mandriva.org> 1:0.6.45-3mdv2010.1
+ Revision: 501882
- rebuild for new boost

* Wed Feb 03 2010 Funda Wang <fwang@mandriva.org> 1:0.6.45-2mdv2010.1
+ Revision: 500297
- use patch rather than env

* Thu Dec 24 2009 Götz Waschk <waschk@mandriva.org> 1:0.6.45-1mdv2010.1
+ Revision: 482019
- update to new version 0.6.45

* Tue Sep 22 2009 Götz Waschk <waschk@mandriva.org> 1:0.6.44-1mdv2010.0
+ Revision: 447187
- update to new version 0.6.44

* Fri Aug 21 2009 Funda Wang <fwang@mandriva.org> 1:0.6.41-3mdv2010.0
+ Revision: 418827
- rebuild for new libboost

* Wed Jul 29 2009 Götz Waschk <waschk@mandriva.org> 1:0.6.41-2mdv2010.0
+ Revision: 402910
- fix python dep

* Tue Jul 28 2009 Götz Waschk <waschk@mandriva.org> 1:0.6.41-1mdv2010.0
+ Revision: 401413
- update build deps
- new version
- drop patches
- new major
- update file list
- add python module

* Wed Mar 25 2009 Emmanuel Andry <eandry@mandriva.org> 1:0.6.27-4mdv2009.1
+ Revision: 361174
- fix string format not literal (fix from upstream git)

* Tue Mar 24 2009 Emmanuel Andry <eandry@mandriva.org> 1:0.6.27-3mdv2009.1
+ Revision: 360890
- add P0 to fix compatibility with evolution pst-import plugin

* Tue Mar 24 2009 Emmanuel Andry <eandry@mandriva.org> 1:0.6.27-2mdv2009.1
+ Revision: 360848
- deal with epoch and libs

* Tue Mar 24 2009 Emmanuel Andry <eandry@mandriva.org> 1:0.6.27-1mdv2009.1
+ Revision: 360817
- downgrade to 0.6.27, the current version has an incompatible ABI with evolution plugin
- drop uneeded patch

* Sun Mar 22 2009 Emmanuel Andry <eandry@mandriva.org> 0.6.34-3mdv2009.1
+ Revision: 360553
- BR gettext-devel
- libpst replaces pst-utils
- diff P0 because define.h is not packaged

* Sun Mar 22 2009 Emmanuel Andry <eandry@mandriva.org> 0.6.34-2mdv2009.1
+ Revision: 360504
- package libification

* Sun Mar 22 2009 Emmanuel Andry <eandry@mandriva.org> 0.6.34-1mdv2009.1
+ Revision: 360420
- import libpst


