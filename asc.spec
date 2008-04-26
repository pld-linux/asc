# TODO:
# - check sounds - doesn't work for me
# - check unpacked files

Summary:	Advanced Strategic Command - a free, turn based strategy game
Summary(pl.UTF-8):	Advanced Strategic Command - turowa gra strategiczna
Name:		asc
Version:	2.1.0.0
Release:	0.1
License:	GPL v2+
Group:		X11/Applications/Games/Strategy
Source0:	http://dl.sourceforge.net/asc-hq/%{name}-%{version}.tar.bz2
# Source0-md5:	d76cf500bebdddd8e7d2a094b532e6af
Source1:	%{name}.desktop
Source2:	%{name}.xpm
URL:		http://www.asc-hq.org/
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_mixer-devel >= 1.2
BuildRequires:	SDL_sound-devel
BuildRequires:	SDL-devel >= 1.2.2
#BuildRequires:	autoconf
#BuildRequires:	automake
BuildRequires:	boost-regex-devel
BuildRequires:	bzip2-devel >= 1.0.0
BuildRequires:	expat-devel
BuildRequires:	freetype-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libsigc++12-devel >= 1.2
#BuildRequires:	libtool >= 2:1.5
BuildRequires:	physfs-devel
BuildRequires:	pkgconfig
Obsoletes:	asc-music
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ASC is a turn-based strategy game in the tradition of Battle Isle 2/3.
It can be played against the computer or against other human players
(either hotseat or by mail).

%description -l pl.UTF-8
ASC jest turową grą strategiczną mającą korzenie w Battle Isle 2/3.
Grając w nią można się zmierzyć z komputerem lub z innym człowiekiem
(przy jednym komputerze, lub przez pocztę).

%prep
%setup -q

# some problems with autotools in this version,
# probably different versions of one of the build tools
%build
#%%{__libtoolize}
#%%{__aclocal}
#%%{__autoconf}
#%%{__autoheader}
#%%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog source/TODO 
%attr(2755,root,games) %{_bindir}/%{name}
%attr(755,root,root) %{_bindir}/asc_mapedit
%{_datadir}/games/%{name}
%{_desktopdir}/%{name}.desktop
%{_mandir}/man6/%{name}.6*
%{_mandir}/man6/asc_mapedit.6*
%{_pixmapsdir}/%{name}.xpm
