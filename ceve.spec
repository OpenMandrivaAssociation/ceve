%define	name	ceve
%define	version	1.0
%define	release	%mkrel 0.rc1.1

Summary:	Dose components for EDOS Ceve
Name:		%{name}
Version:	%{version}
Release:	%{release}
URL:		http://edos-project.org/xwiki/bin/view/Main/Ceve
License:	GPL
Group:		Development/Other
Source0:	%{name}-%{version}rc1.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	ocaml ocaml-calendar-devel ocamlfind-mini ocamlduce
BuildRequires:	ocaml-expat-devel edos-dose mysql-devel rpm-devel

%description
Ceve is a generalized package metadata parser; i.e. it can read
package metadata in several different formats and, after some simple
manipulations, output them in another format. 

%prep
%setup -q %{name}-%{version}rc1

%build
make CFLAGS="-I%{_libdir}/ocaml -I/usr/include/rpm -I/usr/include/mysql" LDFLAGS="-L/usr/lib/mysql"  ceve.opt

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{ocaml_sitelib}
for i in util io mmap lifetime dosebase
	do cd $i; make -I ../make install OCAMLFIND_INSTFLAGS="-destdir %{buildroot}%{ocaml_sitelib}"; cd -
done

%files
%defattr(-,root,root)
