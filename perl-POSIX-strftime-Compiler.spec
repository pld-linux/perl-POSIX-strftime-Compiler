#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	POSIX
%define		pnam	strftime-Compiler
%include	/usr/lib/rpm/macros.perl
Summary:	POSIX::strftime::Compiler - GNU C library compatible strftime for loggers and servers
Name:		perl-POSIX-strftime-Compiler
Version:	0.42
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/POSIX/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	c0a5f76b1b0ce9cdb90d627b017e6cf5
URL:		https://metacpan.org/release/POSIX-strftime-Compiler/
BuildRequires:	perl-Module-Build
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
POSIX::strftime::Compiler provides GNU C library compatible strftime(3). But this module will not affected
by the system locale.  This feature is useful when you want to write loggers, servers and portable applications.

For generate same result strings on any locale, POSIX::strftime::Compiler wraps POSIX::strftime and 
converts some format characters to perl code

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a eg $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/POSIX/strftime
%{_mandir}/man3/POSIX::strftime::Compiler.3*
%{_examplesdir}/%{name}-%{version}
