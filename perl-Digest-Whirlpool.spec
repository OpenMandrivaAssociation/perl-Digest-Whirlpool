%define	upstream_name	 Digest-Whirlpool
%define upstream_version 1.09

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	6

Summary:	Perl 512-bit one-way hash
License:	GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://search.cpan.org/CPAN/authors/id/A/AV/AVAR/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel

%description
Digest::Whirlpool is a 512-bit, collision-resistant, one-way hash function.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make OPTIMIZE="%{optflags}"

%check
make test

%install
%makeinstall_std

%files
%doc README Changes
%{_bindir}/whirlpoolsum
%{_mandir}/*/*
%{perl_vendorarch}/Digest/*.pm
%{perl_vendorarch}/auto/Digest/Whirlpool


%changelog
* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.90.0-4
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Sun May 29 2011 Funda Wang <fwang@mandriva.org> 1.90.0-3
+ Revision: 681424
- mass rebuild

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 1.90.0-2mdv2011.0
+ Revision: 555248
- rebuild

* Fri Nov 06 2009 Jérôme Quelin <jquelin@mandriva.org> 1.90.0-1mdv2010.1
+ Revision: 460840
- update to 1.09

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 1.0.6-5mdv2010.0
+ Revision: 430414
- rebuild

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 1.0.6-4mdv2009.0
+ Revision: 256687
- rebuild

* Tue Jan 15 2008 Thierry Vignaud <tv@mandriva.org> 1.0.6-2mdv2008.1
+ Revision: 152068
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Mon Jul 16 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.6-1mdv2008.0
+ Revision: 52489
- update to new version 1.0.6

* Fri May 04 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 1.0.5-1mdv2008.0
+ Revision: 22424
- New version


* Fri Mar 31 2006 Austin Acton <austin@mandriva.org> 1.0.3-1mdk
- initial package

