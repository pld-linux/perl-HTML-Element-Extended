#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	HTML
%define		pnam	Element-Extended
Summary:	Package of several enhanced HTML::Element* classes
Summary(pl.UTF-8):	Pakiet z kilkoma rozszerzonymi klasami HTML::Element*
Name:		perl-HTML-Element-Extended
Version:	1.18
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/HTML/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	41ec9dcc7cefa03b204d0e8ca8e1c112
URL:		http://search.cpan.org/dist/HTML-Element-Extended/
%if %{with tests}
BuildRequires:	perl(Data::Dumper)
BuildRequires:	perl-HTML-Tree >= 3.01
BuildRequires:	perl(HTML::Element) >= 3.01
%endif
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
HTML-Element-Extended is a package of several enhanced HTML::Element
classes, most of which arose during the effort to implement an
HTML::Element based table class.

The modules are: HTML::ElementTable, HTML::ElementSuper,
HTML::ElementGlob, HTML::ElementRaw.

The resulting functionality enables: tables, element globs, element
coordinates, content replacement, content wrapping, element cloning,
raw HTML string adoption.

%description -l pl.UTF-8
HTML-Element-Extended to pakiet z kilkoma rozszerzonymi klasami
HTML::Element, z których większość powstała podczas próby
zaimplementowania klas opartych na HTML::Element.

Moduły składowe to: HTML::ElementTable, HTML::ElementSuper,
HTML::ElementGlob, HTML::ElementRaw.

Wynikowa funkcjonalność obejmuje: tabele, maski elementów, współrzędne
elementów, zmianę zawartości, zawijanie zawartości, klonowanie
elementów, adopcję surowych łańcuchów HTML.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/HTML/ElementGlob.pm
%{perl_vendorlib}/HTML/ElementRaw.pm
%{perl_vendorlib}/HTML/ElementSuper.pm
%{perl_vendorlib}/HTML/ElementTable.pm
%{_mandir}/man3/HTML::Element*.3pm*
