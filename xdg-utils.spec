%define		pre	rc1

Summary:	Set of tools that assist applications with desktop integration
Name:		xdg-utils
Version:	1.1.0
Release:	0.%{pre}.1
License:	MIT
Group:		X11/Applications
Source0:	http://portland.freedesktop.org/download/%{name}-%{version}-%{pre}.tar.gz
# Source0-md5:	fadf5e7a08e0526fc60dbe3e5b7ef8d6
URL:		http://portland.freedesktop.org/wiki/XdgUtils
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	xmlto
BuildArch:	noarch
Requires:	coreutils
Requires:	which
Requires:	xorg-app-xprop
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xdg-utils is a set of command line tools that assist applications with
a variety of desktop integration tasks. About half of the tools focus
on tasks commonly required during the installation of a desktop
application and the other half focuses on integration with the desktop
environment while the application is running.

%prep
%setup -qn %{name}-%{version}-%{pre}

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README TODO
%attr(755,root,root) %{_bindir}/xdg-desktop-icon
%attr(755,root,root) %{_bindir}/xdg-desktop-menu
%attr(755,root,root) %{_bindir}/xdg-email
%attr(755,root,root) %{_bindir}/xdg-icon-resource
%attr(755,root,root) %{_bindir}/xdg-mime
%attr(755,root,root) %{_bindir}/xdg-open
%attr(755,root,root) %{_bindir}/xdg-screensaver
%attr(755,root,root) %{_bindir}/xdg-settings
%{_mandir}/man1/xdg-desktop-icon.1.*
%{_mandir}/man1/xdg-desktop-menu.1.*
%{_mandir}/man1/xdg-email.1.*
%{_mandir}/man1/xdg-icon-resource.1.*
%{_mandir}/man1/xdg-mime.1.*
%{_mandir}/man1/xdg-open.1.*
%{_mandir}/man1/xdg-screensaver.1.*
%{_mandir}/man1/xdg-settings.1.*

