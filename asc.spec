Summary:	Advanced Strategic Command - a free, turn based strategy game
Summary(pl):	Advanced Strategic Command - turowa gra strategiczna
Name:		asc
Version:	1.10.2
Release:	1
License:	GPL
Group:		X11/Applications/Games/Strategy
Source0:	ftp://ftp.sourceforge.net/pub/sourceforge/asc-hq/%{name}-source-%{version}.tar.gz
Source1:	%{name}.desktop
Patch0:		%{name}-configure.patch
URL:		http://www.asc-hq.org/
BuildRequires:	SDL-devel
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	SDLmm-devel
BuildRequires:	paragui-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
ASC is a free, turn based strategy game. It is designed in the
tradition of the Battle Isle series from Bluebyte and is currently
available for Windows and Linux.

%description -l pl
ASC jest darmow±, turow± gr± strategiczn±. Zosta³a zaprojektowana
w tradycji serii Battle Isle firmy Bluebyte. Obecnie jest dostêpna
pod Windows i Linuksa.
      
%prep
%setup -q
#%patch -p1

%build
%{__libtoolize}
aclocal
%{__automake}
%{__autoconf}
%configure CPPFLAGS="-I%{_includedir}" LDFLAGS="-L%{_libdir}" --disable-paraguitest
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_applnkdir}/Games/Strategy,%{_mandir}/man6,%{_docdir}/%{name}-%{version}/html/graphics}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Games/Strategy
install doc/manpages/*.6 $RPM_BUILD_ROOT%{_mandir}/man6

# bug in make install, so we do it here
install data/*.con $RPM_BUILD_ROOT%{_datadir}/games/asc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc TODO README AUTHORS ChangeLog doc/readme.* doc/graphics doc/*.html doc/*.css
%attr(2755,root,games) %{_bindir}/*
%{_datadir}/games/asc
%{_applnkdir}/Games/Strategy/*
%{_mandir}/man6/*
