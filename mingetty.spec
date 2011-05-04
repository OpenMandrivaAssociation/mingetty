Summary: 	A compact getty program for virtual consoles only
Name: 		mingetty
Version: 	1.08
Release: 	%mkrel 7
Group: 		System/Base
License:	GPL
URL:		http://mingetty.sourceforge.net/
Source0: 	http://downloads.sourceforge.net/mingetty/%{name}-%{version}.tar.gz
Patch0:		mingetty-1.00-opt.patch
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
The mingetty program is a lightweight, minimalist getty program for
use only on virtual consoles.  Mingetty is not suitable for serial
lines (you should use the mgetty program instead for that purpose).

%prep
%setup -q
%patch0 -p1 -b .opt

%build
%serverbuild

%make RPM_OPTS="%{optflags}" LDFLAGS="%{ldflags}"

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}
install -D mingetty %{buildroot}/sbin/mingetty
install -D mingetty.8 %{buildroot}%{_mandir}/man8/mingetty.8

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%doc COPYING
%attr(755,root,root) /sbin/mingetty
%{_mandir}/man8/mingetty.8*
