Summary:	When is an extremely simple personal calendar program
Summary(hu.UTF-8):	When egy végtelenül egyszerű személyi naptár program
Name:		when
Version:	1.1.27
Release:	0.1
License:	GPL v2
Group:		Applications
Source0:	http://www.lightandmatter.com/%{name}/when.tar.gz
# Source0-md5:	11c2b4fa6cc428dc28d947cd33b5e493
URL:		http://www.lightandmatter.com/when/when.html
BuildRequires:	perl-base
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
When is an extremely simple personal calendar program, aimed at the
Unix geek who wants something minimalistic.

%description -l hu.UTF-8
When egy végtelenül egyszerű személyi naptár program, azoknak a Unix
"geek"-eknek, akik valami nagyon egyszerűt akarnak.

%prep
%setup -q -n %{name}_dist

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/when
%{_mandir}/man1/*
%doc README
