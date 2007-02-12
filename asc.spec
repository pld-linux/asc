# TODO:
# - check build
# package probalby Req:  paragui1-devel not paragui-devel

Summary:	Advanced Strategic Command - a free, turn based strategy game
Summary(pl.UTF-8):	Advanced Strategic Command - turowa gra strategiczna
Name:		asc
Version:	1.15.3.0
Release:	0.1
License:	GPL
Group:		X11/Applications/Games/Strategy
Source0:	http://dl.sourceforge.net/asc-hq/%{name}-source-%{version}.tar.gz
# Source0-md5:	5b1259915e48dfd9a44d5ac72ceaea6c
Source1:	%{name}.desktop
Source2:	http://www.asc-hq.org/frontiers.mp3
# Source2-md5:	560f5783836b309906e57e77417f3864
Source3:	http://www.asc-hq.org/time_to_strike.mp3
# Source3-md5:	f0ab3c633f51430af0445ecaa02e3197
Source4:	http://www.asc-hq.org/machine_wars.mp3
# Source4-md5:	c383139928613c7b081835c3d4a28fa8
URL:		http://www.asc-hq.org/
BuildRequires:	SDL-devel
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	SDLmm-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libsigc++12-devel
BuildRequires:	libtool
BuildRequires:	paragui-devel >= 1.0.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ASC is a turn-based strategy game in the tradition of Battle Isle 2/3.
It can be played against the computer or against other human players
(either hotseat or by mail).

%description -l pl.UTF-8
ASC jest turową grą strategiczną mającą korzenie w Battle Isle 2/3.
Grając w nią można się zmierzyć z komputerem lub z innym człowiekiem
(przy jednym komputerze, lub przez pocztę).

%package music
Summary:	Music for Advanced Strategic Command
Summary(pl.UTF-8):	Muzyka do Advanced Strategic Command
Group:		X11/Applications/Games/Strategy
Requires:	%{name}

%description music
Music for Advanced Strategic Command in MP3 format.

%description music -l pl.UTF-8
Muzyka do Advanced Strategic Command w formacie MP3.

%prep
%setup -q

cp %{SOURCE2} %{SOURCE3} %{SOURCE4} data/music

%build
#%{__libtoolize}
#%{__aclocal}
#%{__automake}
#%{__autoconf}
cp -f /usr/share/automake/config.sub .

%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_applnkdir}/Games/Strategy,%{_mandir}/man6,%{_docdir}/%{name}-%{version}/html/graphics}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install data/legacy.con $RPM_BUILD_ROOT%{_datadir}/games/asc

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Games/Strategy

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog source/TODO doc/graphics doc/*.{html,css}
%attr(2755,root,games) %{_bindir}/asc
%attr(755,root,root) %{_bindir}/asc_mapedit
%dir %{_datadir}/games/asc
%dir %{_datadir}/games/asc/music
%{_datadir}/games/asc/*.gfx
%{_datadir}/games/asc/*.zip
%{_datadir}/games/asc/*.con
%{_applnkdir}/Games/Strategy/*

%files music
%defattr(644,root,root,755)
%{_datadir}/games/asc/music/*
