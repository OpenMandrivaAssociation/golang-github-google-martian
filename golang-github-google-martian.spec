# Run tests in check section
%bcond_without check

# https://github.com/google/martian
%global goipath         github.com/google/martian
Version:                2.1.0

%global common_description %{expand:
Martian Proxy is a programmable HTTP proxy designed to be used for testing.

Martian is a great tool to use if you want to:

 - Verify that all (or some subset) of requests are secure
 - Mock external services at the network layer
 - Inject headers, modify cookies or perform other mutations of HTTP requests 
   and responses
 - Verify that pingbacks happen when you think they should
 - Unwrap encrypted traffic (requires install of CA certificate in browser)

By taking advantage of Go cross-compilation, Martian can be deployed anywhere 
that Go can target.}

%gometa

Name:           %{goname}
Release:        1%{?dist}
Summary:        Library for building custom HTTP/S proxies
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires: golang(golang.org/x/net/websocket)

%description
%{common_description}


%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{common_description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%forgeautosetup


%install
%goinstall


%if %{with check}
%check
# https://github.com/google/martian/issues/271
%gochecks -t marbl -t static -d body
%endif


%files devel -f devel.file-list
%license LICENSE
%doc README.md


%changelog
* Fri Oct 05 2018 Robert-André Mauchin <zebob.m@gmail.com> - 2.1.0-1
- First package for Fedora

