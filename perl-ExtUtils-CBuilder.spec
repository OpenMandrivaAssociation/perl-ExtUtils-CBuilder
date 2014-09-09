%define modname	ExtUtils-CBuilder
%define modver 0.280219

Summary:	Compile and link C code for Perl modules 
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	1
License:	GPL or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/ExtUtils/%{modname}-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl(File::Basename)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(Test)
BuildRequires:	perl(Text::ParseWords)
BuildRequires:	perl-devel

%description
This module can build the C portions of Perl modules by invoking the
appropriate compilers and linkers in a cross-platform manner. It was motivated
by the Module::Build project, but may be useful for other purposes as well.
However, it is not intended as a general cross-platform interface to all your C
building needs. That would have been a much more ambitious goal!

%prep
%setup -qn %{modname}-%{modver} 

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
