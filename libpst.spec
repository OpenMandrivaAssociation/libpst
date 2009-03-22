Summary:            Utilities to convert Outlook .pst files to other formats
Name:               libpst
Version:            0.6.34
Release:            1%{?dist}
License:            GPLv2+
Group:              Applications/Productivity
Source:             http://www.five-ten-sg.com/%{name}/packages/%{name}-%{version}.tar.gz
BuildRoot:          %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
URL:                http://www.five-ten-sg.com/%{name}/
Requires:           ImageMagick
BuildRequires:      ImageMagick
BuildRequires:      freetype-devel		
BuildRequires:      gd-devel
BuildRequires:      jpeg-devel
BuildRequires:      zlib-devel

%description
The Libpst utilities include readpst which can convert email messages
to both mbox and MH mailbox formats, pst2ldif which can convert the
contacts to .ldif format for import into ldap databases, and pst2dii
which can convert email messages to the DII load file format used by
Summation.


%prep
%setup -q


%build
#TODO fix format not a string literal
%define Werror_cflags %nil

%configure2_5x
%make


%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%{_bindir}/*
%{_mandir}/man1/*
%{_mandir}/man5/*
%docdir %{_datadir}/doc/%{name}-%{version}
%{_datadir}/doc/%{name}-%{version}


