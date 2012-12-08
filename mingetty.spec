Summary: 	A compact getty program for virtual consoles only
Name: 		mingetty
Version: 	1.08
Release: 	%mkrel 8
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


%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.08-7mdv2011.0
+ Revision: 666428
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 1.08-6mdv2011.0
+ Revision: 606645
- rebuild

* Sun Mar 14 2010 Oden Eriksson <oeriksson@mandriva.com> 1.08-5mdv2010.1
+ Revision: 519042
- rebuild

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.08-4mdv2010.0
+ Revision: 426132
- rebuild

* Sun Dec 21 2008 Oden Eriksson <oeriksson@mandriva.com> 1.08-3mdv2009.1
+ Revision: 317104
- use %%ldflags

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 1.08-2mdv2009.0
+ Revision: 223262
- rebuild

* Sun Mar 02 2008 Olivier Blin <oblin@mandriva.com> 1.08-1mdv2008.1
+ Revision: 177718
- 1.08 (--loginpause support)
- update URL

* Wed Jan 23 2008 Thierry Vignaud <tv@mandriva.org> 1.07-10mdv2008.1
+ Revision: 157254
- rebuild with fixed %%serverbuild macro

* Tue Jan 15 2008 Oden Eriksson <oeriksson@mandriva.com> 1.07-8mdv2008.1
+ Revision: 153301
- fix the build by dropping the dietlibc build

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed Jul 25 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 1.07-7mdv2008.0
+ Revision: 55260
- rebuild with %%serverbuild option


* Tue Feb 13 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 1.07-6mdv2007.0
+ Revision: 120341
- move binaries to /sbin

* Mon Feb 12 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 1.07-5mdv2007.1
+ Revision: 119912
- Import mingetty

* Sun Jan 01 2006 Mandriva Linux Team <http://www.mandrivaexpert.com/> 1.07-4mdk
- Rebuild

* Wed Jan 26 2005 Oden Eriksson <oeriksson@mandrakesoft.com> 1.07-3mdk
- dotnuke

* Wed Jan 26 2005 Oden Eriksson <oeriksson@mandrakesoft.com> 1.07-2mdk
- provide a dietized mingetty too

* Wed Jun 30 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.07-1mdk
- 1.07
- really compile with $RPM_OPT_FLAGS
- cosmetics

