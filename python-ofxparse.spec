Name:		python-ofxparse
Version:	0.21
Release:	2
Summary:	Tools for working with the OFX (Open Financial Exchange) file format
License:	MIT
Group:		Development/Python
URL:		https://pypi.org/project/ofxparse/
Source0:	ofxparse-0.21.tar.gz
BuildSystem:	python
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(wheel)
BuildRequires:	python%{pyver}dist(setuptools)
BuildArch:	noarch
%description
Tools for working with the OFX (Open Financial Exchange) file format.

%files
%{py_sitedir}/*
