# Waf-Tools

A modern Waf-based C++ build system featuring multi-project and multi-mode builds, native host compiler configurations (MSVC/GCC/Clang), Windows cross-compilation from Linux/WSL2, and automatic dependency configuration tracking.

---

## Features

- **Multi-Project & Multi-Mode Configuration**: Easily build different targets (e.g., `Example1`, `Example2`) in either `debug` or `release` modes.
- **Native Host Toolchains**: 
  - Windows: MSVC toolchain supporting both `x64` and `x86` target architectures.
  - Linux: GCC and Clang configurations.
- **Windows Cross-Compilation (Linux to Windows)**: Compile target Windows executables on a Linux host (WSL2 Ubuntu) using Clang and MinGW.
- **PDB Support**: Support for generating MSVC-compatible `.pdb` debug symbol files alongside the Windows target `.exe` during cross-compilation via LLVM's `lld` linker.
- **Fully Static Linking**: Production-ready static linking flags (standard C++, GCC, and thread runtimes) for standalone Windows executables with no external DLL dependencies.
- **Automatic Configuration Tracking**: Native Waf `autoconfig` extended to track changes to both wscripts and Python files under the `tools/` folder. Modifying any configuration script automatically triggers a configuration update on the next build.

---

## Prerequisites

### On Windows
- Python 3.x
- Visual Studio with C++ Build Tools (MSVC) installed.

### On Linux (Ubuntu / WSL2)
- Python 3.x
- Native development tools:
  ```bash
  sudo apt install build-essential clang lld
  ```
- MinGW cross-compilation packages (for Linux-to-Windows builds):
  ```bash
  sudo apt install g++-mingw-w64-x86-64 mingw-w64-x86-64-dev
  ```

---

## Usage

### 1. Configuration
Initialize the build environment. Waf will automatically detect and configure the appropriate native and cross-compilers:
```bash
./waf configure
```
*(On WSL, run `wsl ./waf configure`)*

### 2. Building a Project
Compile your project targets by passing the project, platform, mode, and architecture:
```bash
# Compile Example1 for Linux
./waf build --project=Example1 --platform=Linux --arch=x86_64 --mode=debug

# Cross-compile Example1 for Windows from Linux
./waf build --project=Example1 --platform=Windows --arch=x64 --mode=debug
```

### Options
- `--project=PROJECT`: The project name to build (e.g. `Example1`, `Example2`).
- `--mode=MODE`: Build mode (`debug` or `release`). Default is `debug`.
- `--platform=PLATFORM`: Target platform (`Windows` or `Linux`).
- `--arch=ARCH`: Target architecture (`x64`, `x86` for Windows; `x86_64` for Linux).

---

## License

This project is licensed under the [MIT License](LICENSE).
