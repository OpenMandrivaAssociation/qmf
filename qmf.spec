# QMF git repository
# https://qt.gitorious.org/qt-labs/messagingframework
# git clone git://gitorious.org/qt-labs/messagingframework.git

%define git 1
#define gitdate %(date +%Y%m%d)
%define gitdate 20110802
%define snap 2011W37

%define major 1
%define libname %mklibname %{name} %{major}
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
Source0:		%{name}-%{version}%{?git:-%{snap}}.tar.xz
Source1:		qmf.sh
Source2:		qmf-messageserver.desktop
Patch0:		fix_docs_installation.patch
Patch1:		qmf-1.2.0-no_rpath_tests_benchmarks.patch
Patch2:		qmf-1.2.0-add_headers.patch
Patch3:		qmf-1.2.0-fix_plugins_and_tests_installation_path_for_x86.patch
Patch4:		qmf-1.2.0-fix_plugins_and_tests_installation_path_for_x86_64.patch
Patch5:		qmf-1.2.0-fix-lib-install-x86_64.patch

BuildRequires:   pkgconfig(QtGui)
BuildRequires:   qt4-assistant qt4-qdoc3
BuildRequires:   fdupes > 1.50-0.PR2.2
Requires:	%{libname} = %{version}-%{release}

%description
The Qt Messaging Framework, QMF, consists of a C++ library and daemon server
process that can be used to build email clients, and more generally software
that interacts with email and mail servers.

This package contains:
 - a server application supporting multiple messaging transport mechanisms.

%files
%defattr(-,root,root,-)
%config %{_sysconfdir}/profile.d/%{name}.sh
%config %{_sysconfdir}/xdg/autostart/messageserver.desktop
%{_bindir}/messageserver
%dir %{_libdir}/qmf/plugins/messageservices/
%{_libdir}/qmf/plugins/messageservices/libimap.so
%{_libdir}/qmf/plugins/messageservices/libpop.so
%{_libdir}/qmf/plugins/messageservices/libqmfsettings.so
%{_libdir}/qmf/plugins/messageservices/libsmtp.so

#--------------------------------------------------------------------
%package -n %{libname}
Summary:	Qt Messaging Framework (QMF) message server support library
Group:		System/Libraries
Obsoletes:	%{_lib}qmfclient1
Obsoletes:	%{_lib}qmfmessageserver1
Obsoletes:	%{_lib}qmfutil1

%description -n %{libname}
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

%files -n %{libname}
%defattr(-,root,root,-)
%{_libdir}/libqmfmessageserver.so.%{major}*
%{_libdir}/libqmfclient.so.%{major}*
%dir %{_libdir}/qmf/
%dir %{_libdir}/qmf/plugins/
%dir %{_libdir}/qmf/plugins/contentmanagers/
%{_libdir}/qmf/plugins/contentmanagers/libqmfstoragemanager.so
%{_libdir}/libqmfutil.so.%{major}*

#--------------------------------------------------------------------
%package -n %{libnamedev}
Summary:	Qt Messaging Framework Development Files
Group:		Development/Other
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}

%description -n %{libnamedev}
The Qt Messaging Framework, QMF, consists of a C++ library and daemon server
process that can be used to build email clients, and more generally software
that interacts with email and mail servers.

This package contains the development files needed to build Qt applications
using Qt Messaging Framework libraries.

%files -n %{libnamedev}
%defattr(-,root,root,-)
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
Requires:	%{libname} = %{version}-%{release}

%description examples
The Qt Messaging Framework, QMF, consists of a C++ library and daemon server
process that can be used to build email clients, and more generally software
that interacts with email and mail servers.

The Messages example client application provides an implementation of standard
functionality for creating and viewing messages.

This package contains an example client application supporting common
messaging functionality.

%files examples
%defattr(-,root,root,-)
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
Requires:	%{libname} = %{version}-%{release}

%description tests
The Qt Messaging Framework, QMF, consists of a C++ library and daemon server
process that can be used to build email clients, and more generally software
that interacts with email and mail servers.

This package contains the tests for Qt Messaging Framework (QMF).

%files tests
%defattr(-,root,root,-)
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
%defattr(-,root,root,-)
%dir %{_docdir}/qmf/
%{_docdir}/qmf/qch/
%{_docdir}/qmf/html/

#--------------------------------------------------------------------
%prep
%setup -qn %{name}-%{version}%{?git:-%{snap}}
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


