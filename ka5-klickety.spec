%define		kdeappsver	18.12.0
%define		qtver		5.9.0
%define		kaname		klickety
Summary:	klickety
Name:		ka5-%{kaname}
Version:	18.12.0
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications/Games
Source0:	http://download.kde.org/stable/applications/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	87b94e4e85750576c47842d1a4ad2f86
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= 5.11.1
BuildRequires:	Qt5Qml-devel >= 5.11.1
BuildRequires:	Qt5Quick-devel >= 5.11.1
BuildRequires:	Qt5Widgets-devel
BuildRequires:	cmake >= 2.8.12
BuildRequires:	gettext-devel
BuildRequires:	ka5-libkdegames-devel >= 18.12.0
BuildRequires:	kf5-extra-cmake-modules >= 5.30.0
BuildRequires:	kf5-kconfig-devel >= 5.30.0
BuildRequires:	kf5-kconfigwidgets-devel >= 5.30.0
BuildRequires:	kf5-kcoreaddons-devel >= 5.30.0
BuildRequires:	kf5-kcrash-devel >= 5.30.0
BuildRequires:	kf5-kdbusaddons-devel >= 5.30.0
BuildRequires:	kf5-kdoctools-devel >= 5.30.0
BuildRequires:	kf5-ki18n-devel >= 5.30.0
BuildRequires:	kf5-kio-devel >= 5.30.0
BuildRequires:	kf5-kwidgetsaddons-devel >= 5.30.0
BuildRequires:	kf5-kxmlgui-devel >= 5.30.0
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Klickety is a simple, yet challenging color matching game modeled
after once famous game of SameGame.The idea behind Klickety is to
completely clear the game board filled with the multicolored marbles.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/klickety
%{_desktopdir}/org.kde.klickety.desktop
%{_desktopdir}/org.kde.ksame.desktop
%{_iconsdir}/hicolor/128x128/apps/klickety.png
%{_iconsdir}/hicolor/128x128/apps/ksame.png
%{_iconsdir}/hicolor/16x16/apps/klickety.png
%{_iconsdir}/hicolor/16x16/apps/ksame.png
%{_iconsdir}/hicolor/22x22/apps/klickety.png
%{_iconsdir}/hicolor/22x22/apps/ksame.png
%{_iconsdir}/hicolor/32x32/apps/klickety.png
%{_iconsdir}/hicolor/32x32/apps/ksame.png
%{_iconsdir}/hicolor/48x48/apps/klickety.png
%{_iconsdir}/hicolor/48x48/apps/ksame.png
%{_iconsdir}/hicolor/64x64/apps/klickety.png
%{_iconsdir}/hicolor/64x64/apps/ksame.png
%{_datadir}/kconf_update/klickety-2.0-inherit-ksame-highscore.pl
%{_datadir}/kconf_update/klickety.upd
%{_datadir}/klickety
%{_datadir}/kxmlgui5/klickety
%{_datadir}/metainfo/org.kde.klickety.appdata.xml
%{_datadir}/metainfo/org.kde.ksame.appdata.xml
%{_datadir}/sounds/klickety
