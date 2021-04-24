%define		kdeappsver	21.04.0
%define		kframever	5.56.0
%define		qtver		5.9.0
%define		kaname		klickety
Summary:	klickety
Name:		ka5-%{kaname}
Version:	21.04.0
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications/Games
Source0:	http://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	0baa13584b0a2950d613f5b82c1f22c4
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= 5.11.1
BuildRequires:	Qt5Qml-devel >= 5.11.1
BuildRequires:	Qt5Quick-devel >= 5.11.1
BuildRequires:	Qt5Widgets-devel
BuildRequires:	cmake >= 2.8.12
BuildRequires:	gettext-devel
BuildRequires:	ka5-libkdegames-devel >= %{kdeappsver}
BuildRequires:	kf5-extra-cmake-modules >= %{kframever}
BuildRequires:	kf5-kconfig-devel >= %{kframever}
BuildRequires:	kf5-kconfigwidgets-devel >= %{kframever}
BuildRequires:	kf5-kcoreaddons-devel >= %{kframever}
BuildRequires:	kf5-kcrash-devel >= %{kframever}
BuildRequires:	kf5-kdbusaddons-devel >= %{kframever}
BuildRequires:	kf5-kdoctools-devel >= %{kframever}
BuildRequires:	kf5-ki18n-devel >= %{kframever}
BuildRequires:	kf5-kio-devel >= %{kframever}
BuildRequires:	kf5-kwidgetsaddons-devel >= %{kframever}
BuildRequires:	kf5-kxmlgui-devel >= %{kframever}
BuildRequires:	ninja
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
	-G Ninja \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%ninja_build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

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
%attr(755,root,root) %{_datadir}/kconf_update/klickety-2.0-inherit-ksame-highscore.pl
%{_datadir}/kconf_update/klickety.upd
%{_datadir}/klickety
%{_datadir}/metainfo/org.kde.klickety.appdata.xml
%{_datadir}/metainfo/org.kde.ksame.appdata.xml
%{_datadir}/sounds/klickety
