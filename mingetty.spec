Summary: 	A compact getty program for virtual consoles only
Name: 		mingetty
Version: 	1.07
Release: 	%mkrel 8
Group: 		System/Base
License:	GPL
URL:		ftp://jurix.jura.uni-sb.de/pub/linux/source/system/daemon/
Source0: 	ftp://jurix.jura.uni-sb.de/pub/linux/source/system/daemons/%{name}-%{version}.tar.bz2
Patch0:		mingetty-1.00-opt.patch
BuildRequires:  dietlibc-devel	>= 0.29
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

make \
    CC="diet gcc" \
    CFLAGS="-Os -Wall -pipe -D_GNU_SOURCE -D_BSD_SOURCE" \
    LDFLAGS="-Os -static -s"

mv mingetty mingetty-DIET
make clean
	    
%make RPM_OPTS="%{optflags}"

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}
install -D mingetty %{buildroot}/sbin/mingetty
install mingetty-DIET %{buildroot}/sbin/mingetty-DIET
install -D mingetty.8 %{buildroot}%{_mandir}/man8/mingetty.8

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%doc COPYING
%attr(755,root,root) /sbin/mingetty
%attr(755,root,root) /sbin/mingetty-DIET
%{_mandir}/man8/mingetty.8*
