#
# Conditional build:
%bcond_without	slp	# SLP announcing
#
Summary:	SAP and SLP announcement for the VLC Media Player
Summary(pl.UTF-8):	Rozgłaszanie SAP i SLP dla odtwarzacza multimediów VLC
Name:		minisapserver
Version:	0.3.8
Release:	1
License:	GPL v2+
Group:		Networking
Source0:	http://download.videolan.org/videolan/miniSAPserver/latest/%{name}-%{version}.tar.xz
# Source0-md5:	e2969e92d8c7af41f22ee29a6214ad11
Patch0:		%{name}-slp.patch
URL:		http://www.videolan.org/
BuildRequires:	libstdc++-devel
%{?with_slp:BuildRequires:	openslp-devel}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SAPserver announces, using the SAP/SDP or the SLP protocols, MPEG2 TS
streams produced by for instance VLS. These announces can be received
by the VLC Media Player o.a.

%description -l pl.UTF-8
SAPserver rozgłasza przy użyciu protokołów SAP/SDP lub SLP strumienie
MPEG2 TS utworzone przez np. VLS. Informacje te mogą być odebrane
następnie np. przez odtwarzacz multimedialny VLC Media Player.

%prep
%setup -q
%patch -P0 -p1

%build
%configure \
	--disable-silent-rules \
	%{?with_slp:--enable-slp}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sap.cfg
%attr(755,root,root) %{_bindir}/sapserver
%{_mandir}/man1/sapserver.1*
