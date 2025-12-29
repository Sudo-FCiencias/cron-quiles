#!/usr/bin/env python3
"""
Ejemplo de formato de evento - Documentación visual.

Este archivo muestra cómo se ve un evento en los diferentes formatos
sin necesidad de ejecutar código.
"""

print("=" * 80)
print("EJEMPLO DE EVENTO PROCESADO")
print("=" * 80)

print("\n📥 EVENTO ORIGINAL (del feed ICS)")
print("-" * 80)
print(
    """
SUMMARY: 🐍 Meetup Python CDMX - Machine Learning con TensorFlow
DESCRIPTION: Aprende sobre Machine Learning y TensorFlow en este meetup.
             Trae tu laptop para seguir el workshop práctico.
URL: https://www.meetup.com/pythonista/events/123456789/
LOCATION: WeWork Insurgentes, Ciudad de México, CDMX
ORGANIZER: CN=Pythonista:mailto:organizer@pythonista.com
DTSTART: 20240315T180000-0600
DTEND: 20240315T200000-0600
UID: pythonista-123456789@meetup.com
"""
)

print("\n1️⃣  FORMATO INTERNO (EventNormalized - Python Object)")
print("-" * 80)
print(
    """
event_norm.title          = "meetup python cdmx machine learning con tensorflow"
event_norm.description    = "Aprende sobre Machine Learning y TensorFlow..."
event_norm.url            = "https://www.meetup.com/pythonista/events/123456789/"
event_norm.location       = "WeWork Insurgentes, Ciudad de México, CDMX"
event_norm.organizer      = "Pythonista"
event_norm.dtstart         = datetime(2024, 3, 15, 18, 0, 0, tzinfo=America/Mexico_City)
event_norm.dtend           = datetime(2024, 3, 15, 20, 0, 0, tzinfo=America/Mexico_City)
event_norm.hash_key        = "meetup python cdmx machine learning con tensorflow_2024-03-15T18:00:00-06:00"
event_norm.tags            = {"python", "ai", "data"}
event_norm.source_url      = "https://www.meetup.com/pythonista/events/ical"
"""
)

print("\n2️⃣  FORMATO JSON (salida con --json)")
print("-" * 80)
print(
    """
{
  "title": "🐍 Meetup Python CDMX - Machine Learning con TensorFlow",
  "description": "Aprende sobre Machine Learning y TensorFlow en este meetup. Trae tu laptop para seguir el workshop práctico.",
  "url": "https://www.meetup.com/pythonista/events/123456789/",
  "location": "WeWork Insurgentes, Ciudad de México, CDMX",
  "organizer": "Pythonista",
  "dtstart": "2024-03-15T18:00:00-06:00",
  "dtend": "2024-03-15T20:00:00-06:00",
  "tags": ["python", "ai", "data"],
  "source": "https://www.meetup.com/pythonista/events/ical"
}
"""
)

print("\n3️⃣  FORMATO ICS (en el archivo .ics)")
print("-" * 80)
print(
    """
BEGIN:VEVENT
SUMMARY:🐍 Meetup Python CDMX - Machine Learning con TensorFlow
DESCRIPTION:Aprende sobre Machine Learning y TensorFlow en este meetup. Trae tu laptop para seguir el workshop práctico.
URL:https://www.meetup.com/pythonista/events/123456789/
LOCATION:WeWork Insurgentes, Ciudad de México, CDMX
ORGANIZER;CN=Pythonista:mailto:organizer@pythonista.com
DTSTART;TZID=America/Mexico_City:20240315T180000
DTEND;TZID=America/Mexico_City:20240315T200000
UID:pythonista-123456789@meetup.com
DTSTAMP:20240115T120000Z
CATEGORIES:python,ai,data
END:VEVENT
"""
)

print("\n4️⃣  COMPARACIÓN: Título Original vs Normalizado")
print("-" * 80)
print(
    """
Original:    "🐍 Meetup Python CDMX - Machine Learning con TensorFlow"
Normalizado: "meetup python cdmx machine learning con tensorflow"

Transformaciones aplicadas:
  ✓ Removidos emojis (🐍)
  ✓ Convertido a lowercase
  ✓ Removida puntuación extra (-)
  ✓ Normalizados espacios múltiples

Propósito: Usado para deduplicación (comparar eventos similares)
"""
)

print("\n5️⃣  DETECCIÓN DE TAGS AUTOMÁTICOS")
print("-" * 80)
print(
    """
El sistema analiza título + descripción y detecta keywords:

Título: "Meetup Python CDMX - Machine Learning con TensorFlow"
Descripción: "...Machine Learning y TensorFlow..."

Keywords detectados:
  - "python" → tag: python
  - "machine learning" → tag: ai
  - "tensorflow" → tag: ai, data

Tags resultantes: {"python", "ai", "data"}
"""
)

print("\n6️⃣  HASH KEY PARA DEDUPLICACIÓN")
print("-" * 80)
print(
    """
hash_key = título_normalizado + fecha_redondeada_a_hora

Ejemplo:
  hash_key = "meetup python cdmx machine learning con tensorflow_2024-03-15T18:00:00-06:00"

Eventos con el mismo hash_key (mismo título + misma hora ±2 horas)
se consideran duplicados y se conserva solo el mejor (con URL válida
y descripción más larga).
"""
)

print("\n" + "=" * 80)
print("📋 RESUMEN DE CAMPOS")
print("=" * 80)
print(
    """
Campo          | Tipo              | Descripción
---------------|-------------------|------------------------------------------
title          | str               | Título original del evento
description    | str               | Descripción completa
url            | str               | URL del evento (puede estar vacía)
location       | str               | Ubicación física o virtual
organizer      | str               | Nombre del organizador
dtstart        | datetime          | Fecha/hora inicio (con timezone)
dtend          | datetime          | Fecha/hora fin (con timezone)
tags           | Set[str]          | Tags automáticos detectados
source         | str               | URL del feed ICS de origen
"""
)

print("\n" + "=" * 80)
