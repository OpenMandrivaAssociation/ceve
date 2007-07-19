%define	name	ceve
%define	version	1.0
%define	release	%mkrel 0.rc1.3

Summary:	A generalized package metadata parser
Name:		%{name}
Version:	%{version}
Release:	%{release}
URL:		http://edos-project.org/xwiki/bin/view/Main/Ceve
License:	GPL
Group:		Development/Other
Source0:	%{name}-%{version}rc1.tar.gz
Patch0:		ceve-1.0rc1-use-camlzip.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	ocaml ocaml-calendar-devel ocamlfind-mini ocamlduce
BuildRequires:	ocaml-expat-devel ocaml-camlzip-devel edos-dose
BuildRequires:	mysql-devel rpm-devel db-devel ncurses-devel

%description
Ceve is a generalized package metadata parser; i.e. it can read
package metadata in several different formats and, after some simple
manipulations, output them in another format. 

%prep
%setup -q -n %{name}-%{version}rc1
%patch0 -p1 -b .camlzip

%build
%make CFLAGS="%{optflags} -I%{_libdir}/ocaml -I/usr/include/rpm -I/usr/include/mysql" LDFLAGS="-L/usr/lib/mysql"  ceve ceve.opt

%install
rm -rf %{buildroot}
install -m755 ceve -D %{buildroot}%{_bindir}/ceve
install -m755 ceve.opt -D %{buildroot}%{_bindir}/ceve.opt

install -m644 ceve.1 -D %buildroot%_mandir/man1/ceve.1

%files
%defattr(-,root,root)
%{_bindir}/ceve*
%_mandir/man1/ceve.1*
