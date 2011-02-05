%define upstream_name  	    ExtUtils-CBuilder
%define upstream_version 0.280202

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1
Summary:	Compile and link C code for Perl modules 
License:	GPL or Artistic
Group:		Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source:     http://www.cpan.org/modules/by-module/ExtUtils/%{upstream_name}-%{upstream_version}.tar.gz
BuildRequires:	perl(File::Basename)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(Test)
BuildRequires:	perl(Text::ParseWords)
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
This module can build the C portions of Perl modules by invoking the
appropriate compilers and linkers in a cross-platform manner. It was motivated
by the Module::Build project, but may be useful for other purposes as well.
However, it is not intended as a general cross-platform interface to all your C
building needs. That would have been a much more ambitious goal!

%prep
%setup -q -n %{upstream_name}-%{upstream_version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make

%check
make test

%install
rm -rf %{buildroot}
%makeinstall_std
for m in ExtUtils::CBuilder.3pm ExtUtils::CBuilder::Platform::Windows.3pm; do
	rm -f %{buildroot}%{_mandir}/man3/$m
done

%clean 
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc Changes
%{perl_vendorlib}/ExtUtils
