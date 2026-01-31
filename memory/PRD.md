# J.R Autos - Car Dealership Website PRD

## Original Problem Statement
Build a modern, professional, mobile-friendly website for a car dealership named J.R Autos in Querétaro, Mexico. Features include: Home, Inventory, Services, About, Contact pages with bilingual support (EN/ES), WhatsApp button, Google Maps integration, contact form, and dark theme matching the logo.

## Business Details
- **Business Name**: J.R Autos
- **Industry**: Auto broker / car dealership
- **Services**: Car leasing and vehicle sales
- **Location**: La Mora, Centro, 76850, Querétaro, Querétaro, Mexico
- **Phone**: +52 448 108 5706
- **Google Rating**: 5.0 stars

## User Personas
1. **Car Buyers**: Local customers looking to purchase quality pre-owned vehicles
2. **Lease Seekers**: Individuals interested in flexible car leasing options
3. **Business Inquiries**: Potential partners or financing institutions

## Core Requirements (Static)
- Professional dark-themed design matching logo colors
- Bilingual support (Spanish/English)
- Mobile-responsive layout
- Contact form with database storage
- WhatsApp integration for quick messaging
- Google Maps for location
- SEO-friendly structure

## What's Been Implemented

### January 31, 2026 - Initial Build
- ✅ Complete website with 5 pages: Home, Inventory, Services, About, Contact
- ✅ Dark theme with charcoal background and silver metallic accents
- ✅ Bilingual language toggle (ES/EN) with full translations
- ✅ Hero section with 5.0 Google rating badge
- ✅ Vehicle inventory grid with MongoDB-backed data
- ✅ Services section with 4 service cards
- ✅ Contact form saving to MongoDB with Resend email notifications
- ✅ Google Maps embed on Contact page
- ✅ WhatsApp floating button
- ✅ Phone click-to-call functionality
- ✅ Responsive navigation with mobile menu
- ✅ Footer with business info and social links
- ✅ Framer Motion animations
- ✅ Vehicle detail page with multi-image gallery
- ✅ Inventory filtering by brand and body type
- ✅ Admin panel at `/admin` route for managing vehicles and messages
- ✅ Admin password set to `autos2026`
- ✅ SEO with react-helmet-async, sitemap.xml, robots.txt

## Tech Stack
- **Frontend**: React, Tailwind CSS, Framer Motion, React Router
- **Backend**: FastAPI, Motor (async MongoDB), Pydantic
- **Database**: MongoDB
- **Integrations**: Resend (email notifications)
- **Fonts**: Custom fonts for branding

## Admin Panel Access
- **URL**: `/admin`
- **Password**: `autos2026`

## Prioritized Backlog

### P0 (Critical)
- ✅ All critical features implemented

### P1 (High Priority)
- [ ] Build image upload feature in admin panel (currently uses URL pasting)
- [ ] Dynamic sitemap generation for SEO

### P2 (Medium Priority)
- [ ] Add "Price" field to vehicle listings
- [ ] Add "Sold" status feature for vehicles
- [ ] Move hardcoded admin email to .env variable

### P3 (Nice to Have)
- [ ] Add customer testimonials section
- [ ] Add blog/news section
- [ ] Add vehicle comparison feature
- [ ] Add financing calculator

## Key API Endpoints
- `POST /api/admin/login` - Admin authentication
- `GET /api/vehicles` - List all vehicles
- `POST /api/vehicles` - Create vehicle (admin)
- `GET /api/vehicles/{id}` - Get single vehicle
- `PUT /api/vehicles/{id}` - Update vehicle (admin)
- `DELETE /api/vehicles/{id}` - Delete vehicle (admin)
- `POST /api/contact` - Submit contact form
- `GET /api/contact-messages` - List messages (admin)

## Next Tasks
1. Build direct image upload feature for admin panel
2. Generate dynamic sitemap with vehicle URLs
3. Add price field to vehicle model
