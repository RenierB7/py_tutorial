# Making contributions

Please follow the structure of the repo, i.e.)
```
> py_tutorial
>    │   ├ index.md
>    │   ├ logo.svg
>    │   ├ references.bib
>    │   ├ requirements.txt
>    │   ├ _config.yml
>    │   └ _toc.yml
>    │
>    └───P\<X\>-part-name
>          │   └ index.ipynb
>          │
>          ├───S1-section-one
>          │       └ index.ipynb
>          │
>          ├───S2-section-two
>          │       └ index.ipynb
>          │
>          └───S3-section-three
>                  └ index.ipynb
```

The build task is automated, and assumes that files are laid out like this.

The build task is defined in .github\workflows\build-and-push-to-pages.yml, and runs on push/pull-request.