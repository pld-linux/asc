Summary:	Advanced Strategic Command - a free, turn based strategy game
Name:		asc
Version:	1.5.14beta
Release:	1
License:	GPL
Group:		X11/Applications/Games/Strategy
Group(de):	X11/Applikationen/Spiele/Strategie
Group(pl):	X11/Aplikacje/Gry/Strategiczne
Source0:	ftp://asc-hq.sourceforge.net/pub/asc-hq/develop/%{name}-1.5.14-beta.src.tar.gz
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
%setup -qn %{name}-1.5.14-beta

%build
CPPFLAGS="-I%{_includedir}"; export CPPFLAGS
LDFLAGS="-L%{_libdir}"; export CPPFLAGS
%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_applnkdir}/Games/Strategy,%{_docdir}/%{name}-%{version}/html/graphics}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Games/Strategy

install doc/graphics/* $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/html/graphics/
install doc/{*.html,*.css} $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/html/

gzip -9nf TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(2755,root,games) %{_bindir}/*
%{_datadir}/games/asc
%{_applnkdir}/Games/Strategy/*
