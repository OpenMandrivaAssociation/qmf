%define snap 2011W41

%define major 1
%define libqmfmessageserver %mklibname qmfmessageserver %{major}
%define libqmfutil %mklibname qmfutil %{major}
%define libqmfclient %mklibname qmfclient %{major}
%define libnamedev %mklibname %{name} -d

Name:		qmf
Summary:		Qt Messaging Framework (QMF)
Group:		Development/Other
Version:		2.0
Release:		%mkrel -c %{snap} 1
License:		LGPLv2.1 with exception or GPLv3
URL:		http://qt.gitorious.org/qt-labs/messagingframework
# git archive --remote git://gitorious.org/qt-labs/messagingframework.git \
# --prefix=%{name}-%{version}-%{snap}/ %{snap} | xz > %{name}-%{version}-%{snap}.tar.xz
Source0:		%{name}-%{version}%{snap}.tar.xz
Source1:		qmf.sh
Source2:		qmf-messageserver.desktop
Patch0:		fix_docs_installation.patch
Patch1:		qmf-1.2.0-no_rpath_tests_benchmarks.patch
Patch2:		qmf-1.2.0-add_headers.patch
Patch3:		qmf-1.2.0-fix_plugins_and_tests_installation_path_for_x86.patch
Patch4:		qmf-1.2.0-fix_plugins_and_tests_installation_path_for_x86_64.patch
Patch5:		qmf-1.2.0-fix-lib-install-x86_64.patch

BuildRequires:   pkgconfig(QtGui)
BuildRequires:   qt4-assistant qt4-qdoc
BuildRequires:   fdupes > 1.50-0.PR2.2
Requires:	%{libqmfmessageserver} = %{version}-%{release}
Requires:	%{libqmfclient} = %{version}-%{release}

%description
The Qt Messaging Framework, QMF, consists of a C++ library and daemon server
process that can be used to build email clients, and more generally software
that interacts with email and mail servers.

This package contains:
 - a server application supporting multiple messaging transport mechanisms.

%files
%config %{_sysconfdir}/profile.d/%{name}.sh
%config %{_sysconfdir}/xdg/autostart/messageserver.desktop
%{_bindir}/messageserver
%dir %{_libdir}/qmf/plugins/messageservices/
%{_libdir}/qmf/plugins/messageservices/libimap.so
%{_libdir}/qmf/plugins/messageservices/libpop.so
%{_libdir}/qmf/plugins/messageservices/libqmfsettings.so
%{_libdir}/qmf/plugins/messageservices/libsmtp.so

#--------------------------------------------------------------------
%package -n %{libqmfmessageserver}
Summary:	Qt Messaging Framework (QMF) message server support library
Group:		System/Libraries

%description -n %{libqmfmessageserver}
The Qt Messaging Framework, QMF, consists of a C++ library and daemon server
process that can be used to build email clients, and more generally software
that interacts with email and mail servers.

The MessageServer application is a daemon, designed to run continuously while
providing services to client applications. It provides messaging transport
functionality, communicating with external servers on behalf of Messaging
Framework client applications. New types of messaging (such as Instant
Messages or video messages) can be handled by the server application without
modification to existing client applications.

This package contains:
 - the message server support library. It provides assistance in developing GUI
   clients that access messaging data.

%files -n %{libqmfmessageserver}
%{_libdir}/libqmfmessageserver.so.%{major}*

#--------------------------------------------------------------------
%package -n %{libqmfclient}
Summary:	Qt Messaging Framework (QMF) client library
Group:		System/Libraries

%description -n %{libqmfclient}
The Qt Messaging Framework, QMF, consists of a C++ library and daemon server
process that can be used to build email clients, and more generally software
that interacts with email and mail servers.

The Client library provides classes giving access to all messages stored on
the device, via a uniform interface. It simplifies the task of creating
messaging client applications, and permits other Messaging Framework
applications to interact with messaging data where appropriate. New types of
messages can be supported by the library without modification to existing
client applications.

This package contains a library for developing applications that work with
messages.

%files -n %{libqmfclient}
%{_libdir}/libqmfclient.so.%{major}*
%dir %{_libdir}/qmf/
%dir %{_libdir}/qmf/plugins/
%dir %{_libdir}/qmf/plugins/contentmanagers/
%{_libdir}/qmf/plugins/contentmanagers/libqmfstoragemanager.so

#--------------------------------------------------------------------
%package -n %{libqmfutil}
Summary:	Qt Messaging Framework (QMF) messaging client utility library
Group:		System/Libraries

%description -n %{libqmfutil}
The Qt Messaging Framework, QMF, consists of a C++ library and daemon server
process that can be used to build email clients, and more generally software
that interacts with email and mail servers.

This package contains the messaging client utility library. It provides
assistance in developing plugins for the Message Server daemon.

%files -n %{libqmfutil}
%{_libdir}/libqmfutil.so.%{major}*

#--------------------------------------------------------------------
%package -n %{libnamedev}
Summary:	Qt Messaging Framework Development Files
Group:		Development/Other
Requires:	pkgconfig(QtGui)
Requires:	qt4-assistant qt4-qdoc3
Requires:	fdupes > 1.50-0.PR2.2
Requires:	%{libqmfmessageserver} = %{version}-%{release}
Requires:	%{libqmfclient} = %{version}-%{release}
Requires:	%{libqmfutil} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}

%description -n %{libnamedev}
The Qt Messaging Framework, QMF, consists of a C++ library and daemon server
process that can be used to build email clients, and more generally software
that interacts with email and mail servers.

This package contains the development files needed to build Qt applications
using Qt Messaging Framework libraries.

%files -n %{libnamedev}
%{_includedir}/qmfmessageserver/
%{_includedir}/qmfclient/
%{_libdir}/libqmfmessageserver.prl
%{_libdir}/libqmfmessageserver.so
%{_libdir}/libqmfutil.so
%{_libdir}/libqmfclient.prl
%{_libdir}/libqmfclient.so
%{_libdir}/pkgconfig/qmfmessageserver.pc
%{_libdir}/pkgconfig/qmfclient.pc

#--------------------------------------------------------------------
%package examples
Summary:	Qt Messaging Framework (QMF) Examples
Group:		System/X11
Requires:	%{libqmfmessageserver} = %{version}-%{release}
Requires:	%{libqmfclient} = %{version}-%{release}
Requires:	%{libqmfutil} = %{version}-%{release}

%description examples
The Qt Messaging Framework, QMF, consists of a C++ library and daemon server
process that can be used to build email clients, and more generally software
that interacts with email and mail servers.

The Messages example client application provides an implementation of standard
functionality for creating and viewing messages.

This package contains an example client application supporting common
messaging functionality.

%files examples
%{_bindir}/messagingaccounts
%{_bindir}/qtmail
%{_bindir}/serverobserver
%dir %{_libdir}/qmf/plugins/composers/
%{_libdir}/qmf/plugins/composers/libemailcomposer.so
%dir %{_libdir}/qmf/plugins/viewers/
%{_libdir}/qmf/plugins/viewers/libgenericviewer.so

#--------------------------------------------------------------------
%package tests
Summary:	Qt Messaging Framework (QMF) Tests
Group:		System/X11
Requires:	%{libqmfmessageserver} = %{version}-%{release}
Requires:	%{libqmfclient} = %{version}-%{release}

%description tests
The Qt Messaging Framework, QMF, consists of a C++ library and daemon server
process that can be used to build email clients, and more generally software
that interacts with email and mail servers.

This package contains the tests for Qt Messaging Framework (QMF).

%files tests
%{_libdir}/qmf/tests/

#--------------------------------------------------------------------
%package doc
Summary:	Qt Messaging Framework (QMF) - documentation
Group:		Books/Howtos
BuildArch:	noarch

%description doc
The Qt Messaging Framework, QMF, consists of a C++ library and daemon server
process that can be used to build email clients, and more generally software
that interacts with email and mail servers.

This package contains the documentation for Qt Messaging Framework (QMF).

%files doc
%dir %{_docdir}/qmf/
%{_docdir}/qmf/qch/
%{_docdir}/qmf/html/

#--------------------------------------------------------------------
%prep
%setup -q
%patch0 -p1 -b .fix_docs_installation
%patch1 -p1 -b .no_rpath_tests_benchmarks
%patch2 -p1 -b .add_headers
%ifarch %ix86
%patch3 -p1 -b .fix_plugins_and_tests_installation_for_arch_x86
%else
%patch4 -p1 -b .fix_plugins_and_tests_installation_for_arch_x86_64
%patch5 -p1 -b .fix-lib-install_for_arch_x86_6x4
%endif

%build
%qmake_qt4 \
    QMF_INSTALL_ROOT=%{_prefix} \
    CONFIG+=syslog

%make

%install
rm -rf %{buildroot}
%makeinstall INSTALL_ROOT=%{buildroot}

mkdir -p %{buildroot}%{_sysconfdir}/profile.d
install -m 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/profile.d/
mkdir -p %{buildroot}%{_sysconfdir}/xdg/autostart
install -m 644 %{SOURCE2} %{buildroot}%{_sysconfdir}/xdg/autostart/messageserver.desktop

%fdupes %{buildroot}%{_includedir}


