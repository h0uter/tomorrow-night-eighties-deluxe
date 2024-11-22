![](.readme/screen.png)

# Tomorrow Night Eighties Deluxe Theme

Welcome to the Tomorrow Night Eighties Deluxe theme for Visual Studio Code! This theme is inspired by the classic Tomorrow Night Eighties color scheme but extended with quality-of-life improvements to enhance your coding experience.

## Why Use Tomorrow Night Eighties Deluxe?

- **Enhanced Readability**: underline external imports to make it clear which code comes from external files.
- **Optimized for Python**: Specifically tested and optimized for Python development, ensuring a smooth and visually appealing coding experience.
- **Based on Proven Themes**: Built upon the popular [Tomorrow and Tomorrow Night Operator Mono Theme](https://github.com/stonebuddha/tomorrow-and-tomorrow-night-operator-mono-theme), bringing you the best of both worlds.

## Recommended Setup

For the best experience, we recommend using this theme together with [basedpyright](https://github.com/detachhead/basedpyright), which provides more detailed semantic tokens for constants.

## Semantic Token Comparison

| Feature                             | Pylance | Basedpyright |
| ----------------------------------- | ------- | ------------ |
| Constants (Capitalized var names)   | 0       | 1            |
| Constants (`Final` type annotation) | 0       | 1            |
| Deprecated                          | 1       | 0            |
| Enums                               | 1       | 0            |

## Development

To release new versions of this theme, use the following command:

```sh
vcse publish major|minor|patch
```
