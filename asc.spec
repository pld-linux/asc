# TODO:
# - check sounds - doesn't work for me

Summary:	Advanced Strategic Command - a free, turn based strategy game
Summary(pl.UTF-8):	Advanced Strategic Command - turowa gra strategiczna
Name:		asc
Version:	2.8.0.2
Release:	3
License:	GPL v2+
Group:		X11/Applications/Games/Strategy
#Source0:	https://github.com/ValHaris/asc-hq/archive/ASC%{dashversion}/%{name}-%{version}.tar.gz
Source0:	http://terdon.asc-hq.org/asc/builds/%{name}-%{version}.tar.bz2
# Source0-md5:	f2dfaa794a3ba800f4095815be5b8009
Source1:	%{name}.desktop
Source2:	%{name}.xpm
Patch0:		%{name}-configure.patch
Patch1:		%{name}-lua.patch
Patch2:		gcc10.patch
URL:		http://www.asc-hq.org/
BuildRequires:	SDL-devel >= 1.2.2
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_mixer-devel >= 1.2
BuildRequires:	SDL_sound-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	boost-devel >= 1.35.0
BuildRequires:	bzip2-devel >= 1.0.0
BuildRequires:	curl-devel >= 7.10.0
BuildRequires:	expat-devel
BuildRequires:	freetype-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libsigc++12-devel >= 1.2
BuildRequires:	libtool >= 2:1.5
BuildRequires:	lua51-devel
BuildRequires:	physfs-devel
BuildRequires:	pkgconfig
BuildRequires:	wxGTK2-unicode-gl-devel
BuildRequires:	xvid-devel
BuildRequires:	zip
BuildRequires:	zlib-devel
Obsoletes:	asc-music
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		specflags	-fpermissive

%description
ASC is a turn-based strategy game in the tradition of Battle Isle 2/3.
It can be played against the computer or against other human players
(either hotseat or by mail).

%description -l pl.UTF-8
ASC jest turową grą strategiczną, która posiada korzenie w Battle Isle
2/3. Grając w nią, można się zmierzyć z komputerem lub z innym
człowiekiem (przy jednym komputerze, lub przez pocztę).

%package tools
Summary:	Tools for ASC
Summary(pl.UTF-8):	Narzedzia dla ASC
Group:		X11/Applications/Games/Strategy

%description tools
Map editor and other tools for ASC.

%description tools -l pl.UTF-8
Edytor map i inne narzędzia dla ASC.

%prep
# upstream tarball is busted, contains 2.8.0.1 dir instead of 2.8.0.2
%setup -q -n asc-2.8.0.1
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1

%build
export CXXFLAGS="%{rpmcxxflags} -std=c++11 -D__EXPORT__="
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with-wx-config="wx-gtk2-unicode-config"
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cp -p %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
cp -p %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog source/TODO
%attr(2755,root,games) %{_bindir}/%{name}
%{_datadir}/games/%{name}
%{_desktopdir}/%{name}.desktop
%{_mandir}/man6/%{name}.6*
%{_pixmapsdir}/%{name}.xpm
%{_datadir}/appdata/asc.appdata.xml

%files tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/asc_demount
%attr(755,root,root) %{_bindir}/asc_mapedit
%attr(755,root,root) %{_bindir}/asc_mount
%attr(755,root,root) %{_bindir}/asc_weaponguide
%{_mandir}/man6/asc_demount.6*
%{_mandir}/man6/asc_mapedit.6*
%{_mandir}/man6/asc_mount.6*
%{_mandir}/man6/asc_weaponguide.6*
