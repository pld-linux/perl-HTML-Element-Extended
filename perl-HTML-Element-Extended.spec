#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	HTML
%define	pnam	Element-Extended
Summary:	Package of several enhanced HTML::Element* classes
Summary(pl):	Pakiet z kilkoma rozszerzonymi klasami HTML::Element*
Name:		perl-HTML-Element-Extended
Version:	1.11
Release:	1
# same as perl
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	377ab235ad20a1c88f8bebf4eaf73f90
%if %{with tests}
BuildRequires:	perl(Data::Dumper)
BuildRequires:	perl-HTML-Tree >= 3.01
BuildRequires:	perl(HTML::Element) >= 3.01
%endif
BuildRequires:	perl-devel >= 5.8.0
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

%description -l pl
HTML-Element-Extended to pakiet z kilkoma rozszerzonymi klasami
HTML::Element, z których wiêkszo¶æ powsta³a podczas próby
zaimplementowania klas opartych na HTML::Element.

Modu³y sk³adowe to: HTML::ElementTable, HTML::ElementSuper,
HTML::ElementGlob, HTML::ElementRaw.

Wynikowa funkcjonalno¶æ obejmuje: tabele, maski elementów, wspó³rzêdne
elementów, zmianê zawarto¶ci, zawijanie zawarto¶ci, klonowanie
elementów, adopcjê surowych ³añcuchów HTML.

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
%{perl_vendorlib}/HTML/Element*.pm
%{_mandir}/man3/*
