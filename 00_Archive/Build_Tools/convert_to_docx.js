#!/usr/bin/env node

const fs = require('fs');
const path = require('path');
const {
  Document,
  Packer,
  Paragraph,
  TextRun,
  Table,
  TableRow,
  TableCell,
  Header,
  Footer,
  AlignmentType,
  HeadingLevel,
  BorderStyle,
  WidthType,
  ShadingType,
  VerticalAlign,
  PageNumber,
  PageBreak,
  LevelFormat,
} = require('docx');

const SOURCE_FILE = '/sessions/festive-wonderful-volta/mnt/ExodusProtocol/Exodus_Protocol_Research_Guide.md';
const OUTPUT_FILE = '/sessions/festive-wonderful-volta/mnt/ExodusProtocol/Exodus_Protocol_Research_Guide.docx';

// Read markdown file
const markdown = fs.readFileSync(SOURCE_FILE, 'utf-8');
const lines = markdown.split('\n');

// Configuration
const PAGE_WIDTH = 12240; // US Letter width in DXA
const PAGE_HEIGHT = 15840; // US Letter height in DXA
const MARGIN = 1440; // 1 inch in DXA
const CONTENT_WIDTH = PAGE_WIDTH - (MARGIN * 2); // 9360 DXA

// Document children
const children = [];

// Numbering configuration for lists
const numbering = {
  config: [
    {
      reference: 'bullets',
      levels: [
        {
          level: 0,
          format: LevelFormat.BULLET,
          text: '•',
          alignment: AlignmentType.LEFT,
          style: {
            paragraph: {
              indent: { left: 720, hanging: 360 },
            },
          },
        },
      ],
    },
    {
      reference: 'numbers',
      levels: [
        {
          level: 0,
          format: LevelFormat.DECIMAL,
          text: '%1.',
          alignment: AlignmentType.LEFT,
          style: {
            paragraph: {
              indent: { left: 720, hanging: 360 },
            },
          },
        },
      ],
    },
  ],
};

// Helper function to process inline formatting
function processInlineFormatting(text) {
  const runs = [];
  let current = '';
  let i = 0;

  while (i < text.length) {
    // Check for bold **text**
    if (text[i] === '*' && text[i + 1] === '*') {
      if (current) {
        runs.push(new TextRun(current));
        current = '';
      }
      i += 2;
      let boldText = '';
      while (i < text.length && !(text[i] === '*' && text[i + 1] === '*')) {
        boldText += text[i];
        i++;
      }
      runs.push(new TextRun({ text: boldText, bold: true }));
      i += 2;
    }
    // Check for italic *text* (but not **)
    else if (text[i] === '*' && text[i + 1] !== '*' && !text.slice(0, i).endsWith('*')) {
      if (current) {
        runs.push(new TextRun(current));
        current = '';
      }
      i++;
      let italicText = '';
      while (i < text.length && text[i] !== '*') {
        italicText += text[i];
        i++;
      }
      runs.push(new TextRun({ text: italicText, italics: true }));
      i++;
    } else {
      current += text[i];
      i++;
    }
  }

  if (current) {
    runs.push(new TextRun(current));
  }

  return runs.length > 0 ? runs : [new TextRun('')];
}

// Parse markdown and create paragraphs
let i = 0;
let inCodeBlock = false;
let currentListType = null; // 'bullet' or 'number'
let isFirstParagraph = true;

while (i < lines.length) {
  const line = lines[i];
  const trimmed = line.trim();

  // Skip empty lines within code blocks
  if (inCodeBlock) {
    if (trimmed.startsWith('```')) {
      inCodeBlock = false;
    }
    i++;
    continue;
  }

  // Handle code blocks
  if (trimmed.startsWith('```')) {
    inCodeBlock = true;
    i++;
    continue;
  }

  // Skip empty lines
  if (!trimmed) {
    // End list if we encounter blank line
    if (currentListType) {
      currentListType = null;
    }
    i++;
    continue;
  }

  // Handle H1 headings
  if (trimmed.startsWith('# ') && !trimmed.startsWith('## ')) {
    const title = trimmed.substring(2).trim();
    children.push(
      new Paragraph({
        heading: HeadingLevel.HEADING_1,
        children: processInlineFormatting(title),
        spacing: { before: 240, after: 240 },
      })
    );
    i++;
    continue;
  }

  // Handle H2 headings
  if (trimmed.startsWith('## ') && !trimmed.startsWith('### ')) {
    const title = trimmed.substring(3).trim();
    children.push(
      new Paragraph({
        heading: HeadingLevel.HEADING_2,
        children: processInlineFormatting(title),
        spacing: { before: 180, after: 180 },
      })
    );
    currentListType = null;
    i++;
    continue;
  }

  // Handle H3 headings
  if (trimmed.startsWith('### ')) {
    const title = trimmed.substring(4).trim();
    children.push(
      new Paragraph({
        heading: HeadingLevel.HEADING_3,
        children: processInlineFormatting(title),
        spacing: { before: 120, after: 120 },
      })
    );
    currentListType = null;
    i++;
    continue;
  }

  // Handle horizontal rules
  if (trimmed === '---' || trimmed === '***' || trimmed === '___') {
    children.push(
      new Paragraph({
        border: {
          bottom: {
            color: '2E75B6',
            space: 1,
            style: BorderStyle.SINGLE,
            size: 6,
          },
        },
        spacing: { before: 120, after: 120 },
        children: [new TextRun('')],
      })
    );
    currentListType = null;
    i++;
    continue;
  }

  // Handle bullet lists
  if (trimmed.startsWith('- ')) {
    const content = trimmed.substring(2).trim();
    children.push(
      new Paragraph({
        numbering: { reference: 'bullets', level: 0 },
        children: processInlineFormatting(content),
      })
    );
    currentListType = 'bullet';
    i++;
    continue;
  }

  // Handle numbered lists
  if (/^\d+\.\s/.test(trimmed)) {
    const content = trimmed.replace(/^\d+\.\s/, '').trim();
    children.push(
      new Paragraph({
        numbering: { reference: 'numbers', level: 0 },
        children: processInlineFormatting(content),
      })
    );
    currentListType = 'number';
    i++;
    continue;
  }

  // Handle block quotes (indented lines starting with >)
  if (trimmed.startsWith('> ')) {
    const content = trimmed.substring(2).trim();
    children.push(
      new Paragraph({
        indent: { left: 720, right: 720 },
        children: [new TextRun({ text: content, italics: true })],
        spacing: { before: 120, after: 120 },
      })
    );
    currentListType = null;
    i++;
    continue;
  }

  // Regular paragraph
  if (trimmed) {
    children.push(
      new Paragraph({
        children: processInlineFormatting(trimmed),
        spacing: { after: 200 },
      })
    );
    currentListType = null;
  }

  i++;
}

// Create the document with styles, headers, and footers
const doc = new Document({
  styles: {
    default: {
      document: {
        run: {
          font: 'Arial',
          size: 24, // 12pt
        },
      },
    },
    paragraphStyles: [
      {
        id: 'Heading1',
        name: 'Heading 1',
        basedOn: 'Normal',
        next: 'Normal',
        quickFormat: true,
        run: {
          size: 32, // 16pt
          bold: true,
          font: 'Arial',
        },
        paragraph: {
          spacing: { before: 240, after: 240 },
          outlineLevel: 0,
        },
      },
      {
        id: 'Heading2',
        name: 'Heading 2',
        basedOn: 'Normal',
        next: 'Normal',
        quickFormat: true,
        run: {
          size: 28, // 14pt
          bold: true,
          font: 'Arial',
        },
        paragraph: {
          spacing: { before: 180, after: 180 },
          outlineLevel: 1,
        },
      },
      {
        id: 'Heading3',
        name: 'Heading 3',
        basedOn: 'Normal',
        next: 'Normal',
        quickFormat: true,
        run: {
          size: 26, // 13pt
          bold: true,
          font: 'Arial',
        },
        paragraph: {
          spacing: { before: 120, after: 120 },
          outlineLevel: 2,
        },
      },
    ],
  },
  numbering,
  sections: [
    {
      properties: {
        page: {
          size: {
            width: PAGE_WIDTH,
            height: PAGE_HEIGHT,
          },
          margin: {
            top: MARGIN,
            right: MARGIN,
            bottom: MARGIN,
            left: MARGIN,
          },
        },
      },
      headers: {
        default: new Header({
          children: [
            new Paragraph({
              children: [new TextRun('The Exodus Protocol — Comprehensive Research Guide')],
              alignment: AlignmentType.CENTER,
              spacing: { after: 100 },
            }),
          ],
        }),
      },
      footers: {
        default: new Footer({
          children: [
            new Paragraph({
              children: [
                new TextRun('Page '),
                new TextRun({
                  children: [PageNumber.CURRENT],
                }),
              ],
              alignment: AlignmentType.CENTER,
            }),
          ],
        }),
      },
      children,
    },
  ],
});

// Write the document
Packer.toBuffer(doc).then((buffer) => {
  fs.writeFileSync(OUTPUT_FILE, buffer);
  console.log(`Document created successfully: ${OUTPUT_FILE}`);
});
