Summary:	A compact getty program for virtual consoles only
Name:		mingetty
Version:	1.08
Release:	21
Group:		System/Base
License:	GPLv2
Url:		https://mingetty.sourceforge.net/
Source0:	http://downloads.sourceforge.net/mingetty/%{name}-%{version}.tar.gz
Patch1:		mingetty-1.08-check_chroot_chdir_nice.patch
Patch2:		mingetty-1.08-openlog_authpriv.patch
Patch3:		mingetty-1.08-limit_tty_length.patch
Patch4:		mingetty-1.08-Allow-login-name-up-to-LOGIN_NAME_MAX-length.patch
Patch5:		mingetty-1.08-Clear-scroll-back-buffer-on-clear-screen.patch

%description
The mingetty program is a lightweight, minimalist getty program for
use only on virtual consoles.  Mingetty is not suitable for serial
lines (you should use the mgetty program instead for that purpose).

%prep
%autosetup -p1

%build
%set_build_flags
%make_build CC=%{__cc} CFLAGS="%{optflags}" LDFLAGS="%{build_ldflags}"

%install
install -D mingetty %{buildroot}/sbin/mingetty
install -D mingetty.8 %{buildroot}%{_mandir}/man8/mingetty.8

%files
%doc COPYING
/sbin/mingetty
%{_mandir}/man8/mingetty.8*
