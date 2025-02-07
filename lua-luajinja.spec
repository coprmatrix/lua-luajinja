%define luarocks_pkg_name luajinja
%define luarocks_pkg_version 0.0.1-1
%define luarocks_pkg_prefix luajinja-0.0.1-1
%define luarocks_pkg_major 0.0.1
%define luarocks_pkg_minor 1


Name: lua-luajinja
Version: %{luarocks_pkg_major}
Release: %{luarocks_pkg_minor}
Summary: Jinja2 template engine implementation written in Lua.
Url: https://github.com/huakim/luajinja
License: LGPL
Source0: luajinja-0.0.1.tar.gz
Source1: luajinja-0.0.1.rockspec
BuildRequires: lua-rpm-macros
Requires(postun): alternatives
Requires(post): alternatives
Provides: %{luadist %{luarocks_pkg_name} = %{luarocks_pkg_version}}
%global __luarocks_requires %{_bindir}/true
%global __luarocks_provides %{_bindir}/true
Requires: %{luadist lua >= 5.1}
Requires: %{luadist lpeg}
%{?luarocks_subpackages:%luarocks_subpackages -f}

%description
  Lupa is a Jinja2 template engine implementation written in Lua 
and supports Lua syntax within tags and variables.
  Lupa was sponsored by the Library of the University of Antwerp.


%prep
%autosetup -p1 -n %{luarocks_pkg_prefix}
%luarocks_prep

%generate_buildrequires
%{?luarocks_buildrequires_echo}
%if %{with check}
%luarocks_generate_buildrequires -c -b
%else
%luarocks_generate_buildrequires -b 
%endif

%build
%{?custom_build}
%if %{defined luarocks_subpackages_build}
%{luarocks_subpackages_build}
%else
%if %{defined luarocks_pkg_build}
%luarocks_pkg_build %{lua_version}
%else
%luarocks_build --local
%endif
%endif

%install
%{?custom_install}
%if %{defined luarocks_subpackages_install}
%{luarocks_subpackages_install}
%else
%if %{defined luarocks_pkg_install}
%luarocks_pkg_install %{lua_version}
%else
%luarocks_install %{luarocks_pkg_prefix}.*.rock
%endif
%endif
%{?lua_generate_file_list}

%check
%if %{with check}
%{?luarocks_check}
%endif

%files %{?lua_files}%{!?lua_files:-f lua_files.list}