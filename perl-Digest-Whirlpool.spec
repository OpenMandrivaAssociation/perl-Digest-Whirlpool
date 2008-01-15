%define	real_name	Digest-Whirlpool
%define	name		perl-%real_name
%define	version		1.0.6
%define	release		%mkrel 2

Summary:	Perl 512-bit one-way hash
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Development/Perl
Source:		http://search.cpan.org/CPAN/authors/id/A/AV/AVAR/%{real_name}-%{version}.tar.bz2
URL:		http://search.cpan.org/dist/%{real_name}/
BuildRequires:	perl-devel
BuildRoot:	%{_tmppath}/%{name}-buildroot

%description
Digest::Whirlpool is a 512-bit, collision-resistant, one-way hash function.

%prep
%setup -q -n %{real_name}-%{version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make OPTIMIZE="$RPM_OPT_FLAGS"

%check
%__make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README Changes
%{_bindir}/whirlpoolsum
%{_mandir}/*/*
%{perl_vendorarch}/Digest/*.pm
%{perl_vendorarch}/auto/Digest/Whirlpool

