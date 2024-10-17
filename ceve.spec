Summary:	Generalized package metadata parser
Name:		ceve
Version:	1.4
Release:	%mkrel 1
URL:		https://gforge.inria.fr/projects/sodiac/
License:	GPLv3+
Group:		Development/Other
Source0:	%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
#chrpath needed to remove invalid rpath : /usr/local/bin in ceve binary
Buildrequires:  ocaml-dose2-devel chrpath
Requires:       ocaml-dose2

%description
Ceve is a command line utility used to parse package metadata
information (in particular package interrelationships such as
dependencies) and convert them to set of constraints that need to be
satisfied by a proper package installation.

%prep
%setup -q

%build
%make ceve.opt
chrpath -d ceve.opt

%install
rm -rf %{buildroot}

export EXCLUDE_FROM_STRIP=1
install -m755 ceve.opt -D %{buildroot}%{_bindir}/ceve
install -m644 ceve.1 -D %{buildroot}%{_mandir}/man1/ceve.1

%files
%defattr(-,root,root)
%{_bindir}/ceve*
%{_mandir}/man1/ceve.1*
