Summary:	Advanced Strategic Command - a free, turn based strategy game
Name:		asc
Version:	1.9.4.3
Release:	1
License:	GPL
Group:		X11/Applications/Games/Strategy
Group(de):	X11/Applikationen/Spiele/Strategie
Group(pl):	X11/Aplikacje/Gry/Strategiczne
Source0:	http://prdownloads.sourceforge.net/asc-hq/%{name}-source-%{version}.tar.gz
Source1:	%{name}.desktop
URL:		http://www.asc-hq.org
BuildRequires:	SDL-devel
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	SDLmm-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description

%prep
%setup -q

%build
aclocal
automake -a
autoconf
%configure CPPFLAGS="-I%{_includedir}" LDFLAGS="-L%{_libdir}"
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_applnkdir}/Games/Strategy,%{_mandir}/man6,%{_docdir}/%{name}-%{version}/html/graphics}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Games/Strategy/
install doc/manpages/*.6 $RPM_BUILD_ROOT%{_mandir}/man6/

# bug in make install, so we do it here
install data/*.con $RPM_BUILD_ROOT%{_datadir}/games/asc

gzip -9nf TODO README AUTHORS ChangeLog

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz doc/readme.* doc/graphics doc/*.html doc/*.css
%attr(2755,root,games) %{_bindir}/*
%{_datadir}/games/asc
%{_applnkdir}/Games/Strategy/*
%{_mandir}/man6/*
