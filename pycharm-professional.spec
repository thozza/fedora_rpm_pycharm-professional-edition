# dont strip bundled binaries because pycharm checks length (!!!) of binary fsnotif
# and if you strip debug stuff from it, it will complain
%define __strip /bin/true
# dont repack jars
%define __jar_repack %{nil}
# there are some python 2 and python 3 scripts so there is no way out to bytecompile them ^_^
%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')

Name:		pycharm-professional
Version:	5.0.1
Release:	1%{?dist}
Summary:	Intelligent Python IDE
Group:      Applications/Development
License:    Apache2
URL:		http://www.jetbrains.com/pycharm/
Source0:    http://download.jetbrains.com/python/%{name}-%{version}.tar.gz
Source1:    pycharm.xml
Source2:    pycharm.desktop
BuildRequires: desktop-file-utils python3-devel python2-devel
Requires: java

%description
The intelligent Python IDE with unique code assistance and analysis,
for productive Python development on all levels

%prep
%setup -q -n pycharm-%{version}

%install
mkdir -p %{buildroot}%{_javadir}/%{name}
mkdir -p %{buildroot}%{_datadir}/%{name}
mkdir -p %{buildroot}%{_datadir}/pixmaps
mkdir -p %{buildroot}%{_datadir}/mime/packages
mkdir -p %{buildroot}%{_datadir}/applications
mkdir -p %{buildroot}%{_bindir}

cp -arf ./{lib,bin,help,helpers,plugins} %{buildroot}%{_javadir}/%{name}/
# this will be in docs
rm -f %{buildroot}%{_javadir}/help/*.pdf
cp -af ./bin/pycharm.png %{buildroot}%{_datadir}/pixmaps/pycharm.png
cp -af %{SOURCE1} %{buildroot}%{_datadir}/mime/packages/%{name}.xml
cp -af %{SOURCE2} %{buildroot}%{_datadir}/pycharm.desktop
ln -s %{_javadir}/%{name}/bin/pycharm.sh %{buildroot}%{_bindir}/pycharm
desktop-file-install                          \
--add-category="Development"                  \
--delete-original                             \
--dir=%{buildroot}%{_datadir}/applications    \
%{buildroot}%{_datadir}/pycharm.desktop

%files
%defattr(-,root,root)
%doc *.txt 
%doc license/
%doc help/*.pdf
%dir %{_datadir}/%{name}
%{_datadir}/applications/pycharm.desktop
%{_datadir}/mime/packages/%{name}.xml
%{_datadir}/pixmaps/pycharm.png
%{_javadir}/%{name}/*
%{_bindir}/pycharm


%changelog
* Tue Dec 08 2015 Tomas Hozza <thozza@gmail.com> - 5.0.1-1
- update to 5.0.1

* Wed Oct 07 2015 Tomas Hozza <thozza@gmail.com> - 4.5.4-1
- update to 4.5.4

* Wed Jun 24 2015 Tomas Hozza <thozza@gmail.com> - 4.5.2-1
- update to 4.5.2

* Tue Jun 02 2015 Tomas Hozza <thozza@gmail.com> - 4.5.1-1
- update to 4.5.1

* Sun Apr 26 2015 Tomas Hozza <thozza@gmail.com> - 4.0.6-1
- update to 4.0.6

* Sat Jan 24 2015 Tomas Hozza <thozza@gmail.com> - 4.0.4-1
- update to 4.0.4

* Fri Nov 21 2014 Petr Hracek <phracek@redhat.com> - 4.0-1
- new upstream version 4.0

* Fri Nov 07 2014 Tomas Hozza <thozza@redhat.com> - 3.4.1-3
- Install the icon with name used in .desktop file

* Thu Jul 31 2014 Tomas Tomecek <ttomecek@redhat.com> - 3.4.1-2
- new upstream version 3.4.1
- sanitize specfile

* Mon Jun 09 2014 Petr Hracek <phracek@redhat.com> - 3.4.1-1
- New upstream version

* Wed May 14 2014 Petr Hracek <phracek@redhat.com> - 3.1.3-1
- Initial package


