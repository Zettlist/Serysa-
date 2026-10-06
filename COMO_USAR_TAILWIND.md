# Tailwind en el sitio de SERYSA

El sitio sigue siendo **HTML estatico**. No hay React, ni build de JS, ni bundler.
Tailwind solo genera un archivo de CSS, `tailwind.css`, para poder pegar componentes
de shadcn / 21st.dev / reactbits sin traducir sus clases a mano.

## La unica regla que importa

**Despues de agregar clases nuevas de Tailwind al HTML, hay que regenerar el CSS:**

```
npm run css
```

Si no lo corres, las clases nuevas no existen en `tailwind.css` y no se ven.
Tailwind v4 solo genera las clases que encuentra escritas en `index.html`.

Mientras editas, esto lo hace solo cada vez que guardas:

```
npm run css:watch
```

## Como pegar un componente de React

1. Copia el JSX.
2. `className=` -> `class=`
3. Los componentes de shadcn (`<Card>`, `<CardContent>`, `<Button>`) son `<div>` y
   `<button>` con clases. Reemplazalos por la etiqueta HTML equivalente.
4. `{variable}` y props: quitalos, pon el valor directo.
5. Corre `npm run css`.

Lo que **no** se puede pegar tal cual: componentes con logica de React (`useState`,
`useEffect`, hooks). Eso hay que portarlo a JS, como se hizo con el DriftWall.

## Colores: ya estan los de la marca

`src/tw.css` mapea los tokens de `:root` al tema de Tailwind. O sea:

| clase             | color            |
|-------------------|------------------|
| `bg-blue-500`     | #0b15ed (marca)  |
| `text-cyan-400`   | #22d3ee          |
| `bg-navy-800`     | #070c47          |
| `bg-gray-50`      | #f7f8ff          |
| `font-display`    | Montserrat       |
| `font-sans`       | Open Sans        |
| `shadow-blue`     | sombra azul marca|

Un componente pegado que traiga `bg-blue-500` sale con el azul de SERYSA, no con
el de fabrica de Tailwind. Los colores que Tailwind trae de serie y no se pisaron
(slate, emerald, etc.) siguen disponibles.

## Dos decisiones tecnicas, y por que

**1. Sin preflight.** El reset de Tailwind arrasaria con los ~75 KB de CSS propio
de `index.html`. Por eso en `src/tw.css` se importan las capas por separado en vez
de usar `@import "tailwindcss"`.

**2. Las utilidades van SIN capa (`@layer`).** `index.html` tiene este reset propio,
sin capa:

```css
*,*::before,*::after{margin:0;padding:0;box-sizing:border-box;}
```

En CSS, lo que esta fuera de una capa le gana a todo lo que este dentro de una,
sin importar la especificidad. Con las utilidades dentro de `@layer utilities`,
ese `*` tumbaba **todos** los `p-*`, `px-*`, `m-*`, `mt-*` (comprobado: `p-6` daba
`0px`). Fuera de capa, `.p-6` le gana a `*` y el espaciado funciona.

El CSS propio del sitio sigue protegido por el orden: el `<link>` de `tailwind.css`
va **antes** del `<style>` de `index.html`, asi que ante misma especificidad gana el
CSS propio. Las utilidades pisan el reset, pero no pisan `.service-card`,
`.btn-primary`, `.testim-card`, etc.

## Deploy

No cambia nada. `tailwind.css` se commitea al repo y `firebase deploy` lo sube como
un archivo estatico mas. `package.json`, `package-lock.json`, `src/` y `node_modules/`
estan excluidos en el `ignore` de `firebase.json`.

## Archivos

| archivo            | que es                                   | se commitea |
|--------------------|------------------------------------------|-------------|
| `src/tw.css`       | fuente: imports + tema                   | si          |
| `tailwind.css`     | generado por `npm run css`               | si          |
| `package.json`     | solo el script `css` y la dependencia    | si          |
| `node_modules/`    | dependencias                             | no (gitignore) |

## Para quitar Tailwind

1. Borra el `<link rel="stylesheet" href="tailwind.css">` de `index.html`.
2. Borra `tailwind.css`, `src/`, `package.json`, `package-lock.json`, `node_modules/`.
3. Quita `package.json`, `package-lock.json` y `src/**` del `ignore` de `firebase.json`.

Nada mas depende de el. Copia de seguridad del estado previo en:
`C:\Users\laura\OneDrive\Escritorio\Serysa_backup_pre_tailwind_2026-09-04\`
