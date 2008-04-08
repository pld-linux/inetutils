# TODO:
# - package ifconfig?
# - rc-scripts for: ftpd,telnetd(?),rlogind,uucpd
# - rc-inetd for: ftpd, telnetd,tftpd,rexecd,rlogind,talkd,uucpd
# - default configs for:
# - inetd and standalone subpackages (where possible): ftpd,telnetd(?),rlogind,uucpd
# - collect Obsoletes for: rexecd,rlogin,rsh,rshd,rlogind,uucpd
# - optional kerberos?
# - put configs for ftpd into /etc/ftpd, not /etc
# - rc-inetd files for inetd
# - remove logger conflict with util-linux
# - collect triggers for upgrade: telnetd
Summary:	Common networking utilities and servers
Summary(pl.UTF-8):	Popularne narzędzia i serwery sieciowe
Name:		inetutils
Version:	1.5
Release:	0.1
License:	GPL
Group:		Networking/Utilities
Source0:	http://ftp.gnu.org/gnu/inetutils/%{name}-%{version}.tar.gz
# Source0-md5:	9e0f1ac040de3168ea785f44e42d585e
# syslogd:
Source1:	%{name}-syslog.conf
Source2:	%{name}-syslog.init
Source3:	%{name}-syslog.logrotate
Source4:	%{name}-syslog.sysconfig
# telnet:
Source10:	%{name}-telnet.desktop
Source11:	%{name}-telnet.png
Source12:	%{name}-telnetd.inetd
# ftp:
Source15:	%{name}-ftp.desktop
Source16:	%{name}-ftp.png
# patches:
Patch0:		%{name}-info.patch
Patch1:		%{name}-nolibs.patch
Patch2:		%{name}-tinfo.patch
URL:		http://www.gnu.org/software/inetutils/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.9
# for config.rpath
BuildRequires:	gettext-devel
BuildRequires:	libwrap-devel
BuildRequires:	pam-devel
BuildRequires:	readline-devel
BuildRequires:	rpmbuild(macros) >= 1.268
BuildRequires:	texinfo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libexecdir	%{_sbindir}

%description
This is a distribution of common networking utilities and servers.
Main package currently contains only some common documentation, all
utilities are in their own packages.

%description -l pl.UTF-8
To jest dystrybucja popularnych narzędzi i serwerów sieciowych. Główny
pakiet zawiera tylko wspólną dokumentację, natomiast wszystkie
narzędzia są w osobnych pakietach.

%package ftp
Summary:	FTP client from GNU inetutils package
Summary(pl.UTF-8):	Klient FTP z pakietu GNU inetutils
Group:		Networking/Utilities
Requires:	%{name} = %{version}-%{release}
Provides:	ftp
Obsoletes:	ftp
Obsoletes:	lukemftp
Obsoletes:	tnftp

%description ftp
FTP client from GNU inetutils package.

%description ftp -l pl.UTF-8
Klient FTP z pakietu GNU inetutils.

%package ftpd
Summary:	FTP server from GNU inetutils package
Summary(pl.UTF-8):	Serwer FTP z pakietu GNU inetutils
Group:		Networking/Daemons
Requires:	%{name} = %{version}-%{release}
Provides:	ftpserver
Obsoletes:	ftpserver
# inetd or standalone

%description ftpd
FTP server from GNU inetutils package.

%description ftpd -l pl.UTF-8
Serwer FTP z pakietu GNU inetutils.

%package inetd
Summary:	inetd server from GNU inetutils package
Summary(pl.UTF-8):	Serwer inetd z pakietu GNU inetutils
Group:		Networking/Daemons
Requires:	%{name} = %{version}-%{release}
Requires:	rc-scripts
Provides:	inetdaemon
Obsoletes:	inetdaemon

%description inetd
inetd server from GNU inetutils package.

%description inetd -l pl.UTF-8
Serwer inetd z pakietu GNU inetutils.

%package logger
Summary:	logger utility from GNU inetutils package
Summary(pl.UTF-8):	Narzędzie logger z pakietu GNU inetutils
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}
Provides:	logger
Obsoletes:	logger
Obsoletes:	util-linux-logger
#Temporary:
Conflicts:	util-linux

%description logger
logger utility from GNU inetutils package.

%description logger -l pl.UTF-8
Narzędzie logger z pakietu GNU inetutils.

%package ping
Summary:	ping utility from GNU inetutils package
Summary(pl.UTF-8):	Narzędzie ping z pakietu GNU inetutils
Group:		Networking/Utilities
Requires:	%{name} = %{version}-%{release}
Provides:	ping
Obsoletes:	iputils-ping
Obsoletes:	ping

%description ping
ping utility from GNU inetutils package.

%description ping -l pl.UTF-8
Narzędzie ping z pakietu GNU inetutils.

%package rexecd
Summary:	rexec server from GNU inetutils package
Summary(pl.UTF-8):	Serwer rexec z pakietu GNU inetutils
Group:		Networking/Daemons
Requires:	%{name} = %{version}-%{release}
Requires:	rc-inetd
Provides:	rexecd
Obsoletes:	rexecd

%description rexecd
rexec server from GNU inetutils package.

%description rexecd -l pl.UTF-8
Serwer rexec z pakietu GNU inetutils.

%package rlogin
Summary:	rlogin client from GNU inetutils package
Summary(pl.UTF-8):	Klient rlogin z pakietu GNU inetutils
Group:		Networking/Utilities
Requires:	%{name} = %{version}-%{release}
Provides:	rlogin
Obsoletes:	rlogin

%description rlogin
rlogin client from GNU inetutils package.

%description rlogin -l pl.UTF-8
Klient rlogin z pakietu GNU inetutils.

%package rlogind
Summary:	rlogin server from GNU inetutils package
Summary(pl.UTF-8):	Serwer rlogin z pakietu GNU inetutils
Group:		Networking/Daemons
Requires:	%{name} = %{version}-%{release}
Provides:	rlogind
Obsoletes:	rlogind
# inetd or standalone

%description rlogind
rlogin server from GNU inetutils package.

%description rlogind -l pl.UTF-8
Serwer rlogin z pakietu GNU inetutils.

%package rsh
Summary:	rsh and rcp clients from GNU inetutils package
Summary(pl.UTF-8):	Programy klienckie rsh i rcp z pakietu GNU inetutils
Group:		Networking/Utilities
Requires:	%{name} = %{version}-%{release}
Provides:	rsh
Obsoletes:	rsh

%description rsh
rsh and rcp clients from GNU inetutils package.

%description rsh -l pl.UTF-8
Programy klienckie rsh i rcp z pakietu GNU inetutils.

%package rshd
Summary:	rsh server from GNU inetutils package
Summary(pl.UTF-8):	Serwer rsh z pakietu GNU inetutils
Group:		Networking/Daemons
Requires:	%{name} = %{version}-%{release}
Requires:	rc-inetd
Provides:	rshd
Obsoletes:	rshd

%description rshd
rsh server from GNU inetutils package.

%description rshd -l pl.UTF-8
Serwer rsh z pakietu GNU inetutils.

%package syslogd
Summary:	syslog daemon from GNU inetutils package
Summary(pl.UTF-8):	Demon sysloga z pakietu GNU inetutils
Group:		Daemons
Requires(post):	fileutils
Requires(post,preun):	/sbin/chkconfig
Requires:	%{name} = %{version}-%{release}
Requires:	logrotate >= 3.2-3
Requires:	rc-scripts
Provides:	syslogd
Provides:	syslogdaemon
Obsoletes:	klogd
Obsoletes:	msyslog
Obsoletes:	syslog-ng
Obsoletes:	syslogd

%description syslogd
syslog daemon from GNU inetutils package.

%description syslogd -l pl.UTF-8
Demon sysloga z pakietu GNU inetutils.

%package talk
Summary:	talk client from GNU inetutils package
Summary(pl.UTF-8):	Klient talk z pakiety GNU inetutils
Group:		Networking/Utilities
Requires:	%{name} = %{version}-%{release}
Provides:	talk
Obsoletes:	ntalk
Obsoletes:	ntalk-client
Obsoletes:	talk

%description talk
talk client from GNU inetutils package.

%description talk -l pl.UTF-8
Klient talk z pakiety GNU inetutils.

%package talkd
Summary:	talk server from GNU inetutils package
Summary(pl.UTF-8):	Serwer talk z pakiety GNU inetutils
Group:		Networking/Daemons
Requires:	%{name} = %{version}-%{release}
Requires:	rc-inetd
Provides:	talkd
Obsoletes:	ntalkd
Obsoletes:	talkd

%description talkd
talk server from GNU inetutils package.

%description talkd -l pl.UTF-8
Serwer talk z pakiety GNU inetutils.

%package telnet
Summary:	telnet client from GNU inetutils package
Summary(pl.UTF-8):	Klient telneta z pakietu GNU inetutils
Group:		Networking/Utilities
Requires:	%{name} = %{version}-%{release}
Provides:	telnet
Obsoletes:	heimdal-telnet
Obsoletes:	krb5-telnet
Obsoletes:	telnet

%description telnet
telnet client from GNU inetutils package.

%description telnet -l pl.UTF-8
Klient telneta z pakietu GNU inetutils.

%package telnetd
Summary:	telnet server from GNU inetutils package
Summary(pl.UTF-8):	Serwer telneta z pakietu GNU inetutils
Group:		Networking/Daemons
Requires:	%{name} = %{version}-%{release}
Requires:	inetdaemon
Requires:	login
Requires:	rc-inetd
Provides:	telnetd
Obsoletes:	telnetd

%description telnetd
telnet server from GNU inetutils package.

%description telnetd -l pl.UTF-8
Serwer telneta z pakietu GNU inetutils.

%package tftp
Summary:	TFTP client from GNU inetutils package
Summary(pl.UTF-8):	Klient TFTP z pakietu GNU inetutils
Group:		Networking/Utilities
Requires:	%{name} = %{version}-%{release}
Provides:	tftp
Obsoletes:	tftp
Obsoletes:	tftp-hpa

%description tftp
TFTP client from GNU inetutils package.

%description tftp -l pl.UTF-8
Klient TFTP z pakietu GNU inetutils.

%package tftpd
Summary:	TFTP server from GNU inetutils package
Summary(pl.UTF-8):	Serwer TFTP z pakietu GNU inetutils
Group:		Networking/Daemons
Requires:	%{name} = %{version}-%{release}
Requires:	rc-inetd
Provides:	tftpdaemon
Obsoletes:	atftpd
Obsoletes:	tftp-server
Obsoletes:	tftpd-hpa
Obsoletes:	tftpdaemon
Obsoletes:	utftpd

%description tftpd
TFTP server from GNU inetutils package.

%description tftpd -l pl.UTF-8
Serwer TFTP z pakietu GNU inetutils.

%package uucpd
Summary:	UUCP server from GNU inetutils package
Summary(pl.UTF-8):	Serwer UUCP z pakietu GNU inetutils
Group:		Networking/Daemons
Requires:	%{name} = %{version}-%{release}
Requires:	rc-scripts
Provides:	uucpd
Obsoletes:	uucpd

%description uucpd
UUCP server from GNU inetutils package.

%description uucpd -l pl.UTF-8
Serwer UUCP z pakietu GNU inetutils.

%package whois
Summary:	whois client from GNU inetutils package
Summary(pl.UTF-8):	Klient whois z pakietu GNU inetutils
Group:		Networking/Utilities
Requires:	%{name} = %{version}-%{release}
Provides:	whois
Obsoletes:	whois

%description whois
whois client from GNU inetutils package.

%description whois -l pl.UTF-8
Klient whois z pakietu GNU inetutils.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

cp -f /usr/share/gettext/config.rpath build-aux

%build
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with-pam \
	--with-wrap

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/etc/{rc.d/init.d,sysconfig/rc-inetd,logrotate.d},/bin,/var/log} \
	$RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	SUIDMODE="-m755"

install %{SOURCE1}	$RPM_BUILD_ROOT%{_sysconfdir}/syslog.conf
install %{SOURCE2}	$RPM_BUILD_ROOT/etc/rc.d/init.d/syslog
install %{SOURCE3}	$RPM_BUILD_ROOT/etc/logrotate.d/syslog
install %{SOURCE4}	$RPM_BUILD_ROOT/etc/sysconfig/syslog
install %{SOURCE10}	$RPM_BUILD_ROOT%{_desktopdir}/telnet.desktop
install %{SOURCE11}	$RPM_BUILD_ROOT%{_pixmapsdir}/telnet.png
install %{SOURCE12}	$RPM_BUILD_ROOT/etc/sysconfig/rc-inetd/telnetd
install %{SOURCE15}	$RPM_BUILD_ROOT%{_desktopdir}/ftp.desktop
install %{SOURCE16}	$RPM_BUILD_ROOT%{_pixmapsdir}/ftp.png

for n in alert debug kernel mail.log messages news.log secure syslog
do
	> $RPM_BUILD_ROOT/var/log/$n
done

# follow FHS
mv $RPM_BUILD_ROOT%{_bindir}/ping $RPM_BUILD_ROOT/bin
# unify path
mv $RPM_BUILD_ROOT%{_bindir}/ping6 $RPM_BUILD_ROOT/bin

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%post syslogd
for n in /var/log/{alert,debug,kernel,mail.log,messages,news.log,secure,syslog}
do
	[ -f $n ] && continue
	> $n
	chmod 640 $n
done

/sbin/chkconfig --add syslog
if [ -f /var/lock/subsys/syslog ]; then
	/etc/rc.d/init.d/syslog restart 1>&2
else
	echo "Run \"/etc/rc.d/init.d/syslog start\" to start syslog daemon." 1>&2
fi

%preun syslogd
if [ "$1" = "0" ]; then
	if [ -f /var/lock/subsys/syslog ]; then
		/etc/rc.d/init.d/syslog stop 1>&2
	fi
	/sbin/chkconfig --del syslog
fi

%triggerpostun -- syslog
/sbin/chkconfig --del syslog
/sbin/chkconfig --add syslog
if [ -f /etc/syslog.conf.rpmsave ]; then
	mv -f /etc/syslog.conf /etc/syslog.conf.rpmnew
	mv -f /etc/syslog.conf.rpmsave /etc/syslog.conf
	echo "Moved /etc/syslog.conf.rpmsave as /etc/syslog.conf"
	echo "Original file from package is avaible as /etc/syslog.conf.rpmnew"
fi

%post telnetd
%service -q rc-inetd reload

%postun telnetd
if [ "$1" = "0" ]; then
	%service -q rc-inetd reload
fi

# Here should come trigger for upgrade from standard telnetd

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README* THANKS TODO
%{_infodir}/*.info*

%files ftp
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ftp
%{_desktopdir}/ftp.desktop
%{_pixmapsdir}/ftp.png
%{_mandir}/man1/ftp.1*

%files ftpd
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/ftpd
%{_mandir}/man8/ftpd.8*

%files inetd
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/inetd
%{_mandir}/man8/inetd.8*

%files logger
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/logger
%{_mandir}/man1/logger.1*

%files ping
%defattr(644,root,root,755)
%doc ping/TODO
%attr(4754,root,adm) /bin/ping
%attr(4754,root,adm) /bin/ping6
%{_mandir}/man8/ping.8*

%files rexecd
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/rexecd
%{_mandir}/man8/rexecd.8*

%files rlogin
%defattr(644,root,root,755)
%attr(4755,root,root) %{_bindir}/rlogin
%{_mandir}/man1/rlogin.1*

%files rlogind
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/rlogind
%{_mandir}/man8/rlogind.8*

%files rsh
%defattr(644,root,root,755)
%attr(4755,root,root) %{_bindir}/rcp
%attr(4755,root,root) %{_bindir}/rsh
%{_mandir}/man1/rcp.1*
%{_mandir}/man1/rsh.1*

%files rshd
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/rshd
%{_mandir}/man8/rshd.8*

%files syslogd
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/syslog.conf
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/syslog
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/logrotate.d/syslog
%attr(754,root,root) /etc/rc.d/init.d/syslog
%attr(640,root,root) %ghost /var/log/*
%attr(755,root,root) %{_sbindir}/syslogd
%{_mandir}/man5/syslog.conf.5*
%{_mandir}/man8/syslogd.8*

%files talk
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/talk
%{_mandir}/man1/talk.1*

%files talkd
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/talkd
%{_mandir}/man8/talkd.8*

%files telnet
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/telnet
%{_desktopdir}/telnet.desktop
%{_pixmapsdir}/telnet.png
%{_mandir}/man1/telnet.1*

%files telnetd
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/rc-inetd/telnetd
%attr(755,root,root) %{_sbindir}/telnetd
%{_mandir}/man8/telnetd.8*

%files tftp
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/tftp
%{_mandir}/man1/tftp.1*

%files tftpd
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/tftpd
%{_mandir}/man8/tftpd.8*

%files uucpd
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/uucpd

%files whois
%defattr(644,root,root,755)
%doc gwhois/{README,TODO}
%attr(755,root,root) %{_bindir}/whois
