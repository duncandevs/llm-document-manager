import { AlertCircle } from "lucide-react"

import {
  Alert,
  AlertDescription,
  AlertTitle,
} from "@/components/ui/alert"

type AlertErrorProps = {
  description: string;
  isShown: boolean;
  className?: string;
};

export function AlertError({ description, isShown, className }: AlertErrorProps) {
  if(!isShown) return null;

  return (
    <Alert variant="destructive" className={className}>
      <AlertCircle className="h-4 w-4" />
      <AlertTitle>Error</AlertTitle>
      <AlertDescription>
        {description}
      </AlertDescription>
    </Alert>
  )
};
