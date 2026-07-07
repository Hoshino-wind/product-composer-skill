# Asset Context Protocol

Use this for named brands, products, venues, portfolios, marketing pages, image-heavy pages, product launches, or any UI where user-provided assets, local assets, imagegen-generated assets, logos, screenshots, product shots, icons, texture, and media treatment shape the result.

## Principle

Visual invention should start from asset context when the subject has one. Assets can be user-provided, already present in the project, or generated through imagegen. Colors and fonts are not enough. Product images, UI screenshots, object materials, logo behavior, generated support imagery, and media constraints often carry the design.

When missing visual assets would make the page generic and authenticity does not require real media, use text-to-image generation instead of leaving the design empty. In Codex, call imagegen before implementation and give every generated result a clear design role.

## Context Questions

Before visual direction, identify:

- user-provided assets
- local project assets
- imagegen-generated assets that could support the direction
- brand mark or wordmark availability
- product screenshots or app states
- product shots, venue shots, object photos, or team portraits
- icon style and illustration style
- existing color roles and type roles
- photography style: crop, light, angle, contrast, texture, people, environment
- media constraints: aspect ratios, transparency, resolution, rights, missing files
- required public facts for named products or venues
- asset gaps that require generated placeholders or explicit omission
- missing visual assets that should trigger text-to-image generation

## Asset Inventory

Use this compact shape:

```text
Asset context:
- User-provided:
- Local:
- Imagegen-generated:
- Must use:
- Can use:
- Missing:
- Text-to-image plan:
- Generate with imagegen:
- Infer only:
- Do not fake:
- Media treatment:
- Risk:
```

## Rules

- Do not invent a logo when a real one is required and unavailable.
- Do not use random stock-like imagery when the user needs to inspect a real product, venue, object, or UI state.
- Do not hide missing assets behind blur, darkness, or atmospheric cropping.
- If a product screenshot is the proof object, make it inspectable.
- If missing visual assets would weaken a website, hero/page experience, portfolio, game, product page, or brand page, call imagegen before implementation to create beautiful role-specific assets: hero object, product scene, environment, texture, transition motif, thumbnail, illustration, or empty state.
- If generated media is acceptable, call imagegen and give the result a clear role: hero object, empty state, background texture, product scene, thumbnail, illustration, icon family, or concept support asset.
- Imagegen-generated assets become first-class assets after selection, but their generated nature must stay clear in the plan when authenticity matters.
- Generated assets may depict invented product scenes, abstracted product metaphors, illustrations, textures, thumbnails, empty states, and non-official support imagery.
- Generated assets must not impersonate official logos, real UI screenshots, real venue/object photos, customer portraits, metrics, certifications, or brand-owned assets.
- If assets are missing, state the gap and design around a realistic placeholder instead of pretending.
- Use omission or placeholders only when image generation is unavailable, the asset must be real/official/user-provided, or the generated asset would create false proof.

## Media Treatment

Define:

- crop: full object, macro, side angle, isometric, portrait, device frame, full-bleed
- integration: standalone image, masked object, embedded in UI, background scene, material texture
- contrast: natural, high-contrast, muted, warm, cool, monochrome
- edge behavior: hard edge, soft fade, shadow, reflection, frame, bleed
- relationship to UI: behind, beside, inside, anchored to, or driving the layout

## Verification

Before final output:

- every visible asset has a role
- generated assets have explicit roles and do not pretend to be official or user-provided
- every missing asset is either replaced honestly or omitted
- product or venue imagery remains inspectable when needed
- generated assets do not redefine the approved direction
- media treatment is consistent across sections
