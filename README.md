# PyDFoam
PyFoam on DeepFlame

## 1 Installed Utilities

### 1.1 Runner-Utilities

> These are utilities that start and control OpenFOAM-Runs. Apart from the features described below they start a little XMLRPC-server through which these runs can be controlled (see Network-Utilities).
>
> Most of the utilities can be used to start parallel runs (the number of processors and a host-file have to be provided, depending on the MPI-implementation. The parallel environment is set up automatically).



### 1.2 Utilities for Logfiles

> These utilities can be used to analyze the output of an OpenFOAM-solver that has been written to a file



### 1.3 Networking Utilities

> Most Runner-Utilities start a Server-thread that makes it possible to contact control an OpenFOAM-run and get information about it. These utilities help to access these servers.
>
> Notes:
>
> - 
>
>   These utilities are beta-qualitiy. They work for my network but have not been tested in other environments
>
>   -  The address of the `pyFoamMetaServer.py` is hardcoded into the sources, but can be overwritten using system-wide configuration-files
>
> - `pyFoamNetShell.py` doesn't need any additional infrastructure. Only the address and the port have to be known



### 1.4 Utilities for Manipulating case data

> These utilities are used for manipulating case date. They are especially useful in scripts that automatically set up simulation runs.

#### 1.4.1 `pyFoamAddEmptyBoundary.py`

Adds an empty patch to the boundary file. Such a patch is needed for some mesh-manipulation utilities.

```
pyFoamAddEmptyBoundary.py <case> <patch>
```

DeepFlame

```
# /<case>/constant/polyMesh/boundary
<patch>
{
	type wall;
	nFaces 0;
	startFace <str(lastFace)>
}
```

#### 1.4.2 `pyFoamChangeBoundaryType.py`

Changes the type of a boundary patch.

```
pyFoamChangeBoundaryType.py <case> <patch> <type>
```

DeepFlame

```
# /<case>/constant/polyMesh/boundary
<patch>
{
	type <type>;
	nFaces 0;
	startFace 3300
}
```

#### 1.4.3 `pyFoamChangeBoundaryName.py`

Changes the name of a boundary patch.

```
pyFoamChangeBoundaryName.py <case> <patch> <newname>
```

DeepFlame

```
# /<case>/constant/polyMesh/boundary
<newname>
{
	type wall;
	nFaces 0;
	startFace 3300
}
```

#### 1.4.4 `pyFoamCreateBoundaryPatches.py`

Creates boundary patches in a field-file by looking at the boundary-file.

？

#### 4.4.5 `pyFoamClearCase.py`

Removes all the timesteps except for the first from a case directory.

```
pyFoamClearCase.py <case>
```

Todo: DeepFlame

#### 4.4.6 `pyFoamPackCase.py`

Packs the essential files (the ones that are needed to run it) of a case into a tar-file for archiving/mailing-purposes

```
pyFoamPackCase.py <case>
```

Todo: + .yaml & Inference.py

#### 4.4.7 `pyFoamCloneCase.py`

Creates a copy of a case with only the most essential files

```
pyFoamCloneCase.py <case> <newdirectory>
```

Todo: + .yaml & Inference.py

#### 4.4.8 `pyFoamCopyLastToFirst.py`

Copy last time-step from one case to the first one of another (making it the initial condition)

```
pyFoamCopyLastToFirst.py <sourcecase> <destinationcase>
```

Todo: DeepFlame

#### 4.4.9 `pyFoamClearInternalField.py`

Clears the solution from the internal field

#### 4.4.10 `pyFoamClearBoundaryValue.py`

Clear non-uniform values from the boundary-fields

#### 4.4.11 `pyFoamInitVCS.py`

Initialize the case for the use with the Version Control System (VCS) of your choice

#### 4.4.12 `pyFoamSymlinkToFile.py`

This utility replaces a symlink with a copy of the file/directories it points to. To be used after a `pyFoamCloneCase.py` in `--symlink-mode`

#### 4.4.13 `pyFoamCompressCases.py`

Goes through a case and compresses single files that are bigger than a certain threshold. Purpose is to shrink cases that were run with the setting `uncompressed` in the `controlDict`



### 1.5 Manipulating dictionaries (from scripts)

> For more complex cases these utilities require an understanding of the syntax/semantics of Python-lists and dictionaries



### 1.6 Paraview related utilities

> Thes utilities require a paraview that is compiled with python-support. They have been only tested with ParaView 3.4 and may not work with other versions.



### 1.7 Other

> Utilities that don't fit any of the other categories.



### 1.8 GUI-Tools

> Stuff that is not purely command-line oriented



### 1.9 Special utilities

> Utilities for special applications