Summary:	A compact getty program for virtual consoles only
Name:		mingetty
Version:	1.08
Release:	17
Group:		System/Base
License:	GPLv2
Url:		http://mingetty.sourceforge.net/
Source0:	http://downloads.sourceforge.net/mingetty/%{name}-%{version}.tar.gz
Patch0:	mingetty-1.00-opt.patch

%description
The mingetty program is a lightweight, minimalist getty program for
use only on virtual consoles.  Mingetty is not suitable for serial
lines (you should use the mgetty program instead for that purpose).

%prep
%setup -q
%apply_patches

%build
%serverbuild

%make RPM_OPTS="%{optflags}" LDFLAGS="%{ldflags}"

%install
install -D mingetty %{buildroot}/sbin/mingetty
install -D mingetty.8 %{buildroot}%{_mandir}/man8/mingetty.8

%files
%doc COPYING
/sbin/mingetty
%{_mandir}/man8/mingetty.8*

