Name:           perl-Mail-RFC822-Address
Version:        0.3
Release:        1%{?dist}
Summary:        Perl extension for validating email addresses according to RFC822
License:        CHECK(GPL+ or Artistic)
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Mail-RFC822-Address/
Source0:        http://www.cpan.org/authors/id/P/PD/PDWARREN/Mail-RFC822-Address-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(CPAN)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
Mail::RFC822::Address validates email addresses against the grammar
described in RFC 822 using regular expressions. How to validate a user
supplied email address is a FAQ (see perlfaq9): the only sure way to see if
a supplied email address is genuine is to send an email to it and see if
the user recieves it. The one useful check that can be performed on an
address is to check that the email address is syntactically valid. That is
what this module does.

%prep
%setup -q -n Mail-RFC822-Address-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Changes
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue May 05 2015 Davide Principi <davide.principi@nethesis.it> 0.3-1
- Specfile autogenerated by cpanspec 1.78.
