%global github_name FeatherNotes

Name:           feathernotes
Version:        1.3.2
Release:        1%{?dist}
Summary:        Lightweight Qt notes manager

License:        GPL-3.0-or-later
URL:            https://github.com/tsujan/%{github_name}
Source0:        %{url}/archive/V%{version}/%{github_name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6PrintSupport)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  pkgconfig(x11-xcb)
BuildRequires:  pkgconfig(hunspell) >= 1.6
BuildRequires:  pkgconfig(xext)

Requires:       hicolor-icon-theme

%description
FeatherNotes is a lightweight Qt hierarchical notes manager for Linux.
It is independent of any desktop environment and has:

* Support for rich text formatting, image embedding and inserting
  editable tables;
* Drag-and-drop capability for moving nodes and also for embedding
  images;
* A tray icon for quick access on any desktop;
* Saving and restoring of size (and also position under X11);
* Compact but complete search and replacement widgets;
* The ability to include searchable tags (hidden info on each node);
* Support for optional node icons;
* Support for local and remote hyperlinks (bookmarks);
* Text zooming;
* Printing and exporting to HTML and PDF;
* Password protection;
* Auto-saving;
* Optional spell checking with Hunspell (if enabled at compilation
  time);
* macOS support; and
* Other features that can be found in its settings, on its menus or when
  it is actually used.

%prep
%autosetup -n %{github_name}-%{version} -p 1

%build
%cmake
%cmake_build

%install
%cmake_install
%find_lang %{name} --with-qt

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{name}.metainfo.xml

%files -f %{name}.lang
%license COPYING
%doc ChangeLog INSTALL NEWS README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/icons/hicolor/scalable/mimetypes/text-%{name}-fnx.svg
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/translations
%{_metainfodir}/%{name}.metainfo.xml
%{_datadir}/mime/packages/%{name}.xml

%changelog
* Tue Dec 23 2025 Basil Crow <me@basilcrow.com> - 1.3.2-1
- Initial packaging
