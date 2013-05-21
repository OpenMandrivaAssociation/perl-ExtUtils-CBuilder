%define upstream_name  	    ExtUtils-CBuilder
%define upstream_version 0.280202

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	7
Summary:	Compile and link C code for Perl modules 
License:	GPL or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source:		http://www.cpan.org/modules/by-module/ExtUtils/%{upstream_name}-%{upstream_version}.tar.gz
BuildRequires:	perl(File::Basename)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(Test)
BuildRequires:	perl(Text::ParseWords)
BuildRequires:	perl-devel
BuildArch:	noarch

%description
This module can build the C portions of Perl modules by invoking the
appropriate compilers and linkers in a cross-platform manner. It was motivated
by the Module::Build project, but may be useful for other purposes as well.
However, it is not intended as a general cross-platform interface to all your C
building needs. That would have been a much more ambitious goal!

%prep
%setup -q -n %{upstream_name}-%{upstream_version} 

%build
%__perl Makefile.PL INSTALLDIRS=vendor
make

%check
make test

%install
%makeinstall_std
for m in ExtUtils::CBuilder.3pm ExtUtils::CBuilder::Platform::Windows.3pm; do
	rm -f %{buildroot}%{_mandir}/man3/$m
done

%files 
%doc Changes
%{perl_vendorlib}/ExtUtils


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 0.280.202-5mdv2012.0
+ Revision: 765225
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 0.280.202-4
+ Revision: 763719
- rebuilt for perl-5.14.x

* Fri Jan 20 2012 Oden Eriksson <oeriksson@mandriva.com> 0.280.202-3
+ Revision: 763062
- rebuild

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.280.202-2
+ Revision: 667132
- mass rebuild

* Sat Feb 05 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.280.202-1
+ Revision: 636176
- new version
- update to new version 0.2802

* Mon Dec 27 2010 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.280.200-2mdv2011.0
+ Revision: 625401
- fix man page conflicts with perl package

* Fri Dec 17 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.280.200-1mdv2011.0
+ Revision: 622684
- update to new version 0.2802

* Sat Nov 13 2010 Jérôme Quelin <jquelin@mandriva.org> 0.270.300-3mdv2011.0
+ Revision: 597094
- rebuild

* Wed Jul 28 2010 Jérôme Quelin <jquelin@mandriva.org> 0.270.300-2mdv2011.0
+ Revision: 562422
- rebuild

* Wed Mar 17 2010 Jérôme Quelin <jquelin@mandriva.org> 0.270.300-1mdv2010.1
+ Revision: 523950
- update to 0.2703

* Tue Feb 23 2010 Jérôme Quelin <jquelin@mandriva.org> 0.270.200-1mdv2010.1
+ Revision: 510068
- update to 0.2702

* Tue Feb 16 2010 Jérôme Quelin <jquelin@mandriva.org> 0.270.100-1mdv2010.1
+ Revision: 506740
- update to 0.2701

* Fri Nov 06 2009 Jérôme Quelin <jquelin@mandriva.org> 0.270.0-1mdv2010.1
+ Revision: 461282
- update to 0.27

* Mon Aug 31 2009 Jérôme Quelin <jquelin@mandriva.org> 0.260.301-1mdv2010.0
+ Revision: 422878
- update to 0.260301

* Tue Aug 25 2009 Jérôme Quelin <jquelin@mandriva.org> 0.260.300-2mdv2010.0
+ Revision: 420977
- rebuild

* Mon Jul 20 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.260.300-1mdv2010.0
+ Revision: 398201
- new version

* Mon Jul 06 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.260.200-1mdv2010.0
+ Revision: 392985
- update to new version 0.2602

* Fri Jul 03 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.260.100-1mdv2010.0
+ Revision: 391948
- update to new version 0.2601

* Sat Jun 27 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.250.0-1mdv2010.0
+ Revision: 389927
- new version

  + Antoine Ginies <aginies@mandriva.com>
    - rebuild

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 0.24-3mdv2009.1
+ Revision: 351736
- rebuild

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 0.24-2mdv2009.1
+ Revision: 351724
- rebuild

* Sun Aug 17 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.24-1mdv2009.0
+ Revision: 272886
- update to new version 0.24

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 0.23-2mdv2009.0
+ Revision: 265360
- rebuild early 2009.0 package (before pixel changes)

* Mon Apr 21 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.23-1mdv2009.0
+ Revision: 196139
- update to new version 0.23

* Sun Feb 10 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.22-1mdv2008.1
+ Revision: 164834
- update to new version 0.22

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Nov 01 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.21-1mdv2008.1
+ Revision: 104500
- update to new version 0.21

* Sun Jul 01 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.19-1mdv2008.0
+ Revision: 46525
- update to new version 0.19


* Fri Jun 16 2006 Scott Karns <scottk@mandriva.org> 0.18-2mdv2007.0
- Updated BuildRequires per META.yml

* Mon Mar 27 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.18-1mdk
- New release 0.18

* Fri Mar 17 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.17-1mdk
- New release 0.17

* Tue Oct 04 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.15-1mdk
- New release 0.15

* Thu Sep 22 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.14-1mdk
- fist mdk package

