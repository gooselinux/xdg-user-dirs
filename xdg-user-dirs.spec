Name:		xdg-user-dirs
Version:	0.12
Release:	4%{?dist}
Summary:	Handles user special directories

Group:		User Interface/Desktops
License:	GPLv2+ and MIT
URL:		http://freedesktop.org/wiki/Software/xdg-user-dirs
Source0:	http://user-dirs.freedesktop.org/releases/%{name}-%{version}.tar.gz
Source1:	xdg-user-dirs.sh

# use fuzzy translations (for Downloads)
# https://bugzilla.redhat.com/show_bug.cgi?id=532399
Patch0:		use-fuzzy.patch
# fix a typo in README
Patch1:		typo.patch
# [mr_IN] [xdg-user-dirs] Missing Translations
# https://bugzilla.redhat.com/show_bug.cgi?id=559161
Patch2:		xdg-user-dirs-0.12-mr_IN_translation.patch
# more translations
# https://bugzilla.redhat.com/show_bug.cgi?id=586397
Patch3:         xdg-user-dirs-translations.patch
Patch4:         xdg-user-dirs-translations-2.patch


BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:	gettext
Requires:	%{_sysconfdir}/X11/xinit/xinitrc.d

%description
Contains xdg-user-dirs-update that updates folders in a users
home directory based on the defaults configured by the administrator.

%prep
%setup -q
%patch0 -p1 -b .use-fuzzy
%patch1 -p1 -b .typo
%patch2 -p1 -b .translation-mr
%patch3 -p1 -b .translations
%patch4 -p1 -b .translations-2

%build
%configure
make %{?_smp_mflags}

cd po
touch *.po
make update-gmo

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/X11/xinit/xinitrc.d
install -p -m 755 %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/X11/xinit/xinitrc.d

%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT


%files -f %{name}.lang
%defattr(-,root,root,-)
%doc NEWS AUTHORS README ChangeLog COPYING
%{_bindir}/*
%config(noreplace) %{_sysconfdir}/xdg/user-dirs.conf
%config(noreplace) %{_sysconfdir}/xdg/user-dirs.defaults
%{_sysconfdir}/X11/xinit/xinitrc.d/*

%changelog
* Wed Aug  4 2010 Tomas Bzatek <tbzatek@redhat.com> - 0.12-4
- Fix translations (#586397)

* Mon May  3 2010 Matthias Clasen <mclasen@redhat.com> - 0.12-3
- Add ml translations
Resolves: #586397

* Wed Jan 27 2010 Tomas Bzatek <tbzatek@redhat.com> - 0.12-2
- Add mr_IN translation (#559161)

* Fri Nov  6 2009 Alexander Larsson <alexl@redhat.com> - 0.12-1
- Update to 0.12 which only has a few new translations of Downloads

* Tue Nov  3 2009 Matthias Clasen <mclasen@redhat.com> - 0.11-2
- Use fuzzy translations (for Downloads)  (#532399)
- Fix a typo in README

* Fri Sep 25 2009 Alexander Larsson <alexl@redhat.com> - 0.11-1
- Update to 0.11

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun May  4 2008 Matthias Clasen <mclasen@redhat.com> - 0.10-3
- Fix source url again
- Fix license tag

* Mon Mar 17 2008 Matthias Clasen <mclasen@redhat.com> - 0.10-2
- Fix Source URL

* Tue Feb 12 2008 Alexander Larsson <alexl@redhat.com> - 0.10-1
- Update to 0.10 (new translations)

* Tue Aug 21 2007 Alexander Larsson <alexl@redhat.com> - 0.9-1
- Update to 0.9 (new translations)

* Tue May 29 2007 Matthias Clasen <mclasen@redhat.com> - 0.8-2
- Fix a possible crash.

* Wed May 16 2007  <alexl@redhat.com> - 0.8-1
- Update to 0.8, (only) fixing bug that always recreated deleted directories (#240139)

* Wed Apr 11 2007 Alexander Larsson <alexl@redhat.com> - 0.6-1
- Update to 0.6 (minor fixes)

* Mon Mar 26 2007 Alexander Larsson <alexl@redhat.com> - 0.5-1
- update to 0.5 (more translations)

* Wed Mar  7 2007 Alexander Larsson <alexl@redhat.com> - 0.4-1
- Update to 0.4

* Thu Mar  1 2007 Alexander Larsson <alexl@redhat.com> - 0.3-1
- Update to 0.3

* Fri Feb 23 2007 Alexander Larsson <alexl@redhat.com> - 0.2-1
- initial version
