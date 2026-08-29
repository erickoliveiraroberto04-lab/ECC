# components/ui

Componentes de interface no padrão shadcn/ui (Radix UI + Tailwind), prontos para copiar em qualquer projeto React/Next.js.

## Proveniência

O `accordion.tsx` foi escrito à mão seguindo a implementação padrão e estável do shadcn/ui, pois este ambiente não tem acesso de rede a `21st.dev` (bloqueado pela política de rede do sandbox). Não é uma cópia baixada literalmente daquele registro, mas segue a mesma API e estrutura.

## Dependências necessárias

Para usar `accordion.tsx` em um projeto real, instale:

```bash
npm install @radix-ui/react-accordion clsx tailwind-merge lucide-react
```

E adicione as keyframes de animação no `tailwind.config.js`:

```js
theme: {
  extend: {
    keyframes: {
      "accordion-down": {
        from: { height: "0" },
        to: { height: "var(--radix-accordion-content-height)" },
      },
      "accordion-up": {
        from: { height: "var(--radix-accordion-content-height)" },
        to: { height: "0" },
      },
    },
    animation: {
      "accordion-down": "accordion-down 0.2s ease-out",
      "accordion-up": "accordion-up 0.2s ease-out",
    },
  },
},
```

## Uso

```tsx
import {
  Accordion,
  AccordionItem,
  AccordionTrigger,
  AccordionContent,
} from "@/components/ui/accordion"

<Accordion type="single" collapsible>
  <AccordionItem value="item-1">
    <AccordionTrigger>Pergunta 1</AccordionTrigger>
    <AccordionContent>Resposta 1.</AccordionContent>
  </AccordionItem>
</Accordion>
```
