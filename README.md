# tomorrow-night-eighties-deluxe README

- recommended to use together with [basedpyright](https://github.com/detachhead/basedpyright) because it provides more detailed semantic tokens for constants.
- based on: <https://github.com/stonebuddha/tomorrow-and-tomorrow-night-operator-mono-theme>
- tested with: Python

## semantic token comparison

| feature             | pylance | basedpyright |
| ------------------- | ------- | ------------ |
| constants (Capital) | 0       | 1            |
| constants (`Final`) | 0       | 1            |
| deprecated          | 1       | 0            |
| enums               | 1       | 0            |

## Development

- to release new versions:
- `vcse publish major|minor|patch`
